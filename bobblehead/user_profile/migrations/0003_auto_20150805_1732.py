# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20150805_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=b'test', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=b'test', max_length=100),
        ),
    ]
