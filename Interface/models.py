# get the django libraries we need
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

# we create the model for a facebook acount
class FacebookAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.IntegerField()
    account_name = models.CharField(max_length=100)

    # we create a Meta class, that the user and the account_name should
    # form a unique key together
    class Meta:
        unique_together = ('user', 'account_name')

# we create the model for the Phillips Hue, that keeps track of the user,
# username, ip_adress and the Facebook account
class PhilipsHue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    related_account = models.ForeignKey(FacebookAccount, on_delete=models.SET_NULL, null=True)

# enable registration for both FacebookAccount and PhilipsHue
admin.site.register(FacebookAccount)
admin.site.register(PhilipsHue)
