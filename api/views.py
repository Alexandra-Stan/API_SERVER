from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers

from .models import *
from .serializers import *


@api_view(['GET'])
def getTaxPayer(request):
    taxPayer = TaxPayer.objects.all()
    serializer = TaxPayerSerializer(taxPayer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDeclaration(request):
    declaration = Declaration.objects.all()
    serializer = DeclarationSerializer(declaration, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOneTaxPayer(request, pk):
    try:
        taxPayer = TaxPayer.objects.get(pk=pk)
        serializer = TaxPayerSerializer(taxPayer, many=False)
        return Response(serializer.data)
    except TaxPayer.DoesNotExist:
        content = {'Error': 'Такого налогоплательщика нет'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def postTaxPayer(request):
    data = request.data
    taxPayer = TaxPayer.objects.create(
        Name=data['Name'],
        Surname=data['SurName'],
        LastName=data['LastName'],
        Adres=data['Adres'],
        Email=data['Email'],
        Phone=data['Phone'],
        WorkPhone=data['WorkPhone'],
        WorkAdres=data['WorkAdres'],
        NameOfOrganization=data['NameOfOrganization'],
        UNP=data['UNP']
    )
    serializer = TaxPayerSerializer(taxPayer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postDeclaration(request):
    data = request.data
    ar1 = VAT.objects.get(id=data['Procent'])
    ar2 = TypeOfActivity.objects.get(id=data['Activity'])
    ar3 = TaxPayer.objects.get(id=data['TaxPayer'])
    declaration = Declaration.objects.create(
        NameOfDeclaration=data['NameOfDeclaration'],
        Income=data['Income'],
        Expense=data['Expense'],
        IncomeNoVAT=data['IncomeNoVAT'],
        NonOperationIncome=data['NonOperationIncome'],
        Nalog=data['Nalog'],
        DayOfDeclare=data['DayOfDeclare'],
        Comment=data['Comment'],
        Draft=data['Draft'],
        LastNalog=data['LastNalog'],
        Procent=ar1,
        Activity=ar2,
        TaxPayer=ar3



    )
    serializer = DeclarationSerializer(declaration, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def putTaxPayer(request, pk):
    data = request.data
    taxPayer = TaxPayer.objects.get(pk=pk)
    serializer = TaxPayerSerializer(instance=taxPayer, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        content = {'Error': 'Заполните все поля'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTaxPayer(request, pk):
    taxPayer = TaxPayer.objects.get(pk=pk)
    taxPayer.delete()
    return Response('Наогоплательщик удален!')

@api_view(['POST'])
def loginPage(request):
    data = request.data
    username = data['username']
    password = data['password']

    print(request.data, username, password)
    if data['username'] in [None, ''] or data['password'] in [None, '']:
        content = {'Error': 'Заполните все поля'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            content = {'Error': 'No such User'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def putVAT(request, pk):
    data = request.data
    vat = VAT.objects.get(pk=pk)
    serializer = VATSerializer(instance=vat, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        content = {'Error': 'Заполните все поля'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)



