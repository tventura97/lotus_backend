from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Accounts

class AccountsViewSet(viewsets.ModelViewSet): 
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'

