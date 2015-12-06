from django.db import models
from django.contrib import admin


# Create your models here.
// here is the database we are going to use to trach words
// for each word, we track whether it is related to some feeling
class Database(models.Model):
    word = models.CharField(max_length=100, unique=True)
    anger = models.BooleanField(default=0)
    anticipation = models.BooleanField(default=0)
    disgust = models.BooleanField(default=0)
    fear = models.BooleanField(default=0)
    joy = models.BooleanField(default=0)
    sadness = models.BooleanField(default=0)
    surprise = models.BooleanField(default=0)
    trust = models.BooleanField(default=0)

admin.site.register(Database)
