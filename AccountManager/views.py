from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountSerializer, OwnedChallengeSerializer, ChallengeSerializer, PhotoSerializer, MomentSerializer
from .models import Account, OwnedChallenge, Challenge, Photo, Moment

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

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class MomentViewSet(viewsets.ModelViewSet):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer