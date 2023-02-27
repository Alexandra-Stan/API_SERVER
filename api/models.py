from django.db import models
from datetime import date

from django.urls import reverse


class VAT(models.Model):
    VATName = models.CharField("Название", max_length=1000)
    VATPersent = models.PositiveSmallIntegerField("Процент", default=0)

    def __str__(self):
        return self.VATName

    class Meta:
        verbose_name = "Процент"
        verbose_name_plural = "Проценты"


class MinistryOfTaxes(models.Model):
    NameOfMinRole = models.CharField("Должность", max_length=1000)

    def __str__(self):
        return self.NameOfMinRole

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class TypeOfActivity(models.Model):
    NameOfActivity = models.CharField("Вид деятельности", max_length=1000)

    def __str__(self):
        return self.NameOfActivity

    class Meta:
        verbose_name = "Вид деятельности"
        verbose_name_plural = "Виды деятельности"


class TaxPayer(models.Model):

    Name = models.CharField("Имя", max_length=1000)
    Surname = models.CharField("Фамилия", max_length=1000)
    LastName = models.CharField("Отчество", max_length=1000)
    Adres = models.CharField("Адресс", max_length=1000)
    Email = models.EmailField("Почта")
    Phone = models.CharField("Телефон", max_length=1000)
    WorkPhone = models.CharField("Рабочий телефон", max_length=1000)
    WorkAdres = models.CharField("Рабочий адресс", max_length=1000)
    NameOfOrganization = models.CharField("Название организации", max_length=1000)
    UNP = models.PositiveIntegerField("УНП", default=0)

    def __str__(self):
        return self.NameOfOrganization

    def get_absolute_url(self):
        return reverse("payer_detail", kwargs={"slug": self.NameOfOrganization})

    class Meta:
        verbose_name = "Налогоплательщик"
        verbose_name_plural = "Налогоплательщики"


class OfficePerson(models.Model):
    Name = models.CharField("Имя", max_length=1000)
    Surname = models.CharField("Фамилия", max_length=1000)
    LastName = models.CharField("Отчество", max_length=1000)
    Adres = models.CharField("Адресс", max_length=1000)
    Email = models.EmailField("Почта")
    Phone = models.CharField("Телефон", max_length=1000)
    WorkPhone = models.CharField("Рабочий телефон", max_length=1000)
    Experience = models.PositiveSmallIntegerField("Опыт работы", default=0)
    Salary = models.PositiveSmallIntegerField("Зарплата", default=0)
    Cabinet = models.PositiveSmallIntegerField("Кабинет", default=0)
    JobTitle = models.ForeignKey(MinistryOfTaxes, on_delete=models.CASCADE, verbose_name="Должность", default=18)

    def __str__(self):
        return self.Surname

    class Meta:
        verbose_name = "Работник налоговой службы"
        verbose_name_plural = "Работники налоговой службы"


class Declaration(models.Model):
    NameOfDeclaration = models.CharField("Имя декларации", max_length=1000)
    Income = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Доход')
    Expense = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Расход')
    IncomeNoVAT = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Не облагаемый доход')
    NonOperationIncome = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Внереализационные доходы')
    Nalog = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Налог')
    DayOfDeclare = models.DateTimeField("Дата подачи")
    Comment = models.CharField("Комментарий", max_length=1000, blank=True)
    Draft = models.BooleanField("Черновик", default=False)
    Procent = models.ForeignKey(VAT, on_delete=models.CASCADE, verbose_name="Процент")
    Activity = models.ForeignKey(TypeOfActivity, on_delete=models.CASCADE, verbose_name="Вид деятельности")
    TaxPayer = models.ForeignKey(TaxPayer, on_delete=models.CASCADE, verbose_name="Налогоплательщик")
    LastNalog = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Налог за прошлый период',
                                    default='100')

    def __str__(self):
        return self.NameOfDeclaration

    def get_absolute_url(self):
        return reverse("declaration_detail", kwargs={"slug": self.url})

    def get_question(self):
        return self.questions_set.filter(parent__isnull=True)



    class Meta:
        verbose_name = "Декларация"
        verbose_name_plural = "Декларации"


class Debetor(models.Model):
    Debt = models.PositiveIntegerField("Долг", default=0)
    DateOfPay = models.DateField("Дата выплаты", default=date.today)
    Payer = models.ManyToManyField(TaxPayer, verbose_name="Налогоплательщик", default=18)

    def __str__(self):
        return self.Payer

    class Meta:
        verbose_name = "Долг"
        verbose_name_plural = "Долги"


class Questions(models.Model):
    Email = models.EmailField("Почта")
    Name = models.CharField("Имя", max_length=1000)
    Question = models.CharField("Вопрос", max_length=5000)
    Topic = models.CharField("Тема", max_length=5000, default='')
    Declaration = models.ForeignKey(Declaration, verbose_name="Декларация", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="Написал", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.Name} - {self.Declaration}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
