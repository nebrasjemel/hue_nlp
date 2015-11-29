from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FacebookAccounts(models.Model):
    username = models.ForeignKey(User)
    account_id = models.IntegerField()
    access_token = models.CharField(max_length=100)

