from rest_framework import serializers
from .models import Account, OwnedChallenge, Challenge, Photo, Moment

class OwnedChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnedChallenge
        fields = ('id', 'title', 'description', 'pointValue', 'status')

class ChallengeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description', 'pointValue')
        lookup_field = 'id'

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url')
        lookup_field = 'id'

class MomentSerializer(serializers.HyperlinkedModelSerializer):
    photo_set = PhotoSerializer(many=True)
    challenge = ChallengeSerializer()
    class Meta:
        model = Moment
        fields = ('id', 'title', 'date', 'challenge', 'description', 'photo_set')

class AccountSerializer(serializers.HyperlinkedModelSerializer): 
    ownedchallenge_set = OwnedChallengeSerializer(many=True)
    moment_set = MomentSerializer(many=True)
    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'firstName', 'lastName', 'level', 'ownedchallenge_set', 'moment_set')
        lookup_field = 'username'
