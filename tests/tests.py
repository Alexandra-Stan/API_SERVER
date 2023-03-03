import datetime
import json

from rest_framework import status
from rest_framework.test import APITestCase
from api.models import *
from datetime import date


class TaxPayerTests(APITestCase):

    def setUp(self):
        self.add_test_payer()

    def delete_all_taxpayer(self):
        TaxPayer.objects.all().delete()

    def add_test_payer(self):
        new_payer = TaxPayer(
            Name="Name",
            Surname='SurName',
            LastName='LastName',
            Adres='Adres',
            Email='email@mail.com',
            Phone='Phone',
            WorkPhone='WorkPhone',
            WorkAdres='WorkAdres',
            NameOfOrganization='NameOfOrganization',
            UNP=123445
        )
        new_payer.save()

    def test_delete_taxpayer(self):
        id = TaxPayer.objects.get().id
        url = f"/api/deleteTaxPayer/{id}/"
        response = self.client.delete(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TaxPayer.objects.count(), 0)

    def test_list_taxpayer(self):
        url = "/api/getTaxPayer/"
        response = self.client.get(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_taxpayer(self):
        id = TaxPayer.objects.get().id
        url = f"/api/deleteTaxPayer/{id}/"
        response = self.client.delete(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TaxPayer.objects.count(), 0)

    def test_list_vat(self):
        url = "/api/getVAT/"
        response = self.client.get(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_declaration(self):
        url = "/api/getDeclaration/"
        response = self.client.get(path=url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_taxpayer(self):
        self.delete_all_taxpayer()
        url = "/api/postTaxPayer/"
        data = {
            "Name": "Name",
            "Surname": "Surname",
            "LastName": "LastName",
            "Adres": "Adres",
            "Email": "ma@mail.ru",
            "Phone": 343432432,
            "WorkPhone": 12345678,
            "WorkAdres": "WorkAdres",
            "NameOfOrganization": "NameOfOrganization",
            "UNP": 11111111111,

        }

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TaxPayer.objects.count(), 1)
        self.assertEqual(TaxPayer.objects.get().Name, 'Name')
        self.assertEqual(TaxPayer.objects.get().Surname, 'Surname')
        self.assertEqual(TaxPayer.objects.get().LastName, 'LastName')
        self.assertEqual(TaxPayer.objects.get().Adres, 'Adres')
        self.assertEqual(TaxPayer.objects.get().Email, 'ma@mail.ru')
        self.assertEqual(TaxPayer.objects.get().Phone, '343432432')
        self.assertEqual(TaxPayer.objects.get().WorkPhone, '12345678')
        self.assertEqual(TaxPayer.objects.get().WorkAdres, 'WorkAdres')
        self.assertEqual(TaxPayer.objects.get().NameOfOrganization, 'NameOfOrganization')
        self.assertEqual(TaxPayer.objects.get().UNP, 11111111111)


#


    def add_test_declaration(self):
        new_declaration = Declaration(
            NameOfDeclaration='NameOfDeclaration',
            Income=133.00,
            Expense=233.00,
            IncomeNoVAT=1456.00,
            NonOperationIncome=5253.00,
            Nalog=12345.00,
            DayOfDeclare='2023-02-27T15:08:33Z',
            Comment='Comment',
            Draft=False,
            LastNalog=134.00,
            Procentet="1",
            Activityy="1",
            Taxpayerr="1"
        )
        print("add ok")
        new_declaration.save()

    def delete_all_declaration(self):
        Declaration.objects.all().delete()

    def test_create_declaration(self):
        self.delete_all_declaration()
        url = "/api/postDeclaration/"
        data = {

            "NameOfDeclaration": "test",
            "Income": "2234.00",
            "Expense": "3454.00",
            "IncomeNoVAT": "34534657.00",
            "NonOperationIncome": "567564.00",
            "Nalog": "457564.00",
            "DayOfDeclare": "2023-02-27T15:08:33Z",
            "Comment": "нет",
            "Draft": False,
            "LastNalog": "100.00",
            "Procentet": 1,
            "Activityy": 1,
            "Taxpayerr": 1

        }
        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Declaration.objects.count(), 1)
        self.assertEqual(Declaration.objects.get().NameOfDeclaration, 'test')
        self.assertEqual(Declaration.objects.get().Income, 2234.00)
        self.assertEqual(Declaration.objects.get().Expense, 3454.00)
        self.assertEqual(Declaration.objects.get().IncomeNoVAT, 34534657.00)
        self.assertEqual(Declaration.objects.get().NonOperationIncome, 567564.00)
        self.assertEqual(Declaration.objects.get().Nalog, 457564.00)
        self.assertEqual(Declaration.objects.get().Comment, 'нет')
        self.assertEqual(Declaration.objects.get().Draft, False)
        self.assertEqual(Declaration.objects.get().LastNalog, 100.00)
        self.assertEqual(Declaration.objects.get().Procentet, "1")
        self.assertEqual(Declaration.objects.get().Activityy, "1")
        self.assertEqual(Declaration.objects.get().Taxpayerr, "1")

    def test_update_declaration(self):
        self.delete_all_declaration()
        self.add_test_declaration()
        id = Declaration.objects.get().id
        url = f"/api/putDeclaration/{id}/"
        data = {

            "NameOfDeclaration": "test2",
            "Income": "2234.00",
            "Expense": "3454.00",
            "IncomeNoVAT": "34534657.00",
            "NonOperationIncome": "567564.00",
            "Nalog": "457564.00",
            "DayOfDeclare": "2023-02-27T15:08:33Z",
            "Comment": "нет",
            "Draft": False,
            "LastNalog": "100.00",
            "Procentet": 1,
            "Activityy": 1,
            "Taxpayerr": 1

        }
        response = self.client.put(path=url, data=json.dumps(data), content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Declaration.objects.count(), 1)
        self.assertEqual(Declaration.objects.get().NameOfDeclaration, 'test2')
        self.assertEqual(Declaration.objects.get().Income, 2234.00)
        self.assertEqual(Declaration.objects.get().Expense, 3454.00)
        self.assertEqual(Declaration.objects.get().IncomeNoVAT, 34534657.00)
        self.assertEqual(Declaration.objects.get().NonOperationIncome, 567564.00)
        self.assertEqual(Declaration.objects.get().Nalog, 457564.00)
        self.assertEqual(Declaration.objects.get().Comment, 'нет')
        self.assertEqual(Declaration.objects.get().Draft, False)
        self.assertEqual(Declaration.objects.get().LastNalog, 100.00)
        self.assertEqual(Declaration.objects.get().Procentet, "1")
        self.assertEqual(Declaration.objects.get().Activityy, "1")
        self.assertEqual(Declaration.objects.get().Taxpayerr, "1")

