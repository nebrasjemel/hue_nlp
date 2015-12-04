# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0002_auto_20151203_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='philipshue',
            name='related_account',
        ),
        migrations.RemoveField(
            model_name='philipshue',
            name='username',
        ),
        migrations.DeleteModel(
            name='PhilipsHue',
        ),
    ]
