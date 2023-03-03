from django.urls import path
from . import views

urlpatterns = [
    path('getOneTaxPayer/<int:pk>/', views.getOneTaxPayer),
    path('getTaxPayer/', views.getTaxPayer),
    path('getVAT/', views.getVAT),
    path('getDeclaration/', views.getDeclaration),
    path('postTaxPayer/', views.postTaxPayer),
    path('postDeclaration/', views.postDeclaration),
    path('putDeclaration/<int:pk>/', views.putDeclaration),
    path('putVAT/<int:pk>/', views.putVAT),
    path('deleteTaxPayer/<int:pk>/', views.deleteTaxPayer),
   # path('login/', views.loginPage, name='login'),

]
