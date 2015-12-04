# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0004_philipshue'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookaccount',
            name='account_name',
            field=models.CharField(default='Facebook', max_length=100),
            preserve_default=False,
        ),
    ]
