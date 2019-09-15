from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountSerializer, OwnedChallengeSerializer, ChallengeSerializer
from .models import Account, OwnedChallenge, Challenge

class AccountsViewSet(viewsets.ModelViewSet): 
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'

class OwnedChallengeViewSet(viewsets.ModelViewSet):
    queryset = OwnedChallenge.objects.all()
    serializer_class = OwnedChallengeSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    lookup_field = 'id'