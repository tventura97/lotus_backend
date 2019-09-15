from django.db import models

# Create your models here.
class OwnedChallenge (models.Model): 
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length=500)
    pointValue = models.IntegerField(default=1)
    status = models.IntegerField(default=0)

class Account (models.Model): 
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    challenges = models.ForeignKey(OwnedChallenge)
