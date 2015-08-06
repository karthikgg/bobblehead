# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
