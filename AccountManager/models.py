from django.db import models

# Create your models here.
class Account (models.Model): 
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    level = models.IntegerField(default=1)

class OwnedChallenge (models.Model): 
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length=500)
    pointValue = models.IntegerField(default=1)
    status = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, default = "")

class Challenge(models.Model): 
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    pointValue = models.IntegerField(default=1)

    def __str__(self): 
        return self.title

class Moment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, default="")
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    challenge = models.ForeignKey(Challenge, on_delete=models.PROTECT, default="")
    description = models.CharField(max_length=500)


class Photo(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, default = "")
    moment = models.ForeignKey(Moment, on_delete=models.PROTECT, default = "")
    url = models.CharField(max_length=200, default = "")


