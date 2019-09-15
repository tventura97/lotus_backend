from django.contrib import admin
from .models import Account, OwnedChallenge, Challenge

# Register your models here.
admin.site.register(Account)
admin.site.register(OwnedChallenge)
admin.site.register(Challenge)