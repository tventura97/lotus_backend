from rest_framework import serializers
from .models import Account, OwnedChallenge

class AccountSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'firstName', 'lastName', 'level', 'challenges')
        lookup_field = 'username'

class OwnedChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnedChallenge
        fields = ('id', 'title', 'description', 'pointValue', 'status')
