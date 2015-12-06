# this is our database
# -*- coding: utf-8 -*-
# import the necessary libraries
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]
    
    # create the model of the database, with the 10 fields
    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('word', models.CharField(unique=True, max_length=100)),
                ('anger', models.BooleanField(default=0)),
                ('anticipation', models.BooleanField(default=0)),
                ('disgust', models.BooleanField(default=0)),
                ('fear', models.BooleanField(default=0)),
                ('joy', models.BooleanField(default=0)),
                ('sadness', models.BooleanField(default=0)),
                ('surprise', models.BooleanField(default=0)),
                ('trust', models.BooleanField(default=0)),
            ],
        ),
    ]
