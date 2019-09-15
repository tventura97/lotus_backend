from rest_framework import serializers
from .models import Account, OwnedChallenge, Challenge

class OwnedChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnedChallenge
        fields = ('id', 'title', 'description', 'pointValue', 'status')

class AccountSerializer(serializers.HyperlinkedModelSerializer): 
    ownedchallenge_set = OwnedChallengeSerializer(many=True)
    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'firstName', 'lastName', 'level', 'ownedchallenge_set')
        lookup_field = 'username'

class ChallengeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description', 'pointValue')
        lookup_field = 'id'