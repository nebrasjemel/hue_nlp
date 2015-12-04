from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.


class FacebookAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.IntegerField()
    access_token = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'account_name',)


class PhilipsHue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    related_account = models.ForeignKey(FacebookAccount, on_delete=models.SET_NULL, null=True)


admin.site.register(FacebookAccount)
admin.site.register(PhilipsHue)
