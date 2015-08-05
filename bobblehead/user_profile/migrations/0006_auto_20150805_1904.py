# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20150805_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='udacity_key',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
