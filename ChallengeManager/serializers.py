from rest_framework import serializers
from .models import Challenge

class ChallengeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description', 'pointValue')
        lookup_field = 'id'