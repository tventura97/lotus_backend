from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ChallengeSerializer
from .models import Challenge

class ChallengeViewSet(viewsets.ModelViewSet): 
    queryset = Challenge.objects.all().order_by('title')
    serializer_class = ChallengeSerializer
    lookup_field = 'id'

