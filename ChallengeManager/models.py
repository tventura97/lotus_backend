from django.db import models

# Create your models here

class Challenge(models.Model): 
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    pointValue = models.IntegerField(default=1)

    def __str__(self): 
        return self.title
