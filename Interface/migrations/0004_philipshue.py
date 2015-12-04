# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Interface', '0003_auto_20151203_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhilipsHue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=15)),
                ('related_account', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='Interface.FacebookAccount', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
