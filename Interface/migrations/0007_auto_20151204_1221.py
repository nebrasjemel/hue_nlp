# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0006_auto_20151204_0059'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='facebookaccount',
            unique_together=set([('user', 'account_name')]),
        ),
    ]
