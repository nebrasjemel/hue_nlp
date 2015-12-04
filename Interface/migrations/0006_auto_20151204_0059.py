# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0005_facebookaccount_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facebookaccount',
            old_name='username',
            new_name='user',
        ),
    ]
