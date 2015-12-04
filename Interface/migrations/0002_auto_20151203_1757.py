# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.IntegerField()),
                ('access_token', models.CharField(max_length=100)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhilipsHue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.CharField(max_length=15)),
                ('related_account', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='Interface.FacebookAccount', null=True)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='facebookaccounts',
            name='username',
        ),
        migrations.RemoveField(
            model_name='philipshues',
            name='related_account',
        ),
        migrations.RemoveField(
            model_name='philipshues',
            name='username',
        ),
        migrations.DeleteModel(
            name='FacebookAccounts',
        ),
        migrations.DeleteModel(
            name='PhilipsHues',
        ),
    ]
