from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import *


class TaxPayerSerializer(ModelSerializer):
    class Meta:
        model =TaxPayer
        fields = '__all__'


class DeclarationSerializer(ModelSerializer):
    class Meta:
        model =Declaration
        fields = '__all__'


class VATSerializer(ModelSerializer):
    class Meta:
        model =VAT
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_superuser', 'groups', 'first_name', 'last_name')