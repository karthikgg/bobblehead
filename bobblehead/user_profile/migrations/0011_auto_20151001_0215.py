# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20150901_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nanodegree',
            field=models.CharField(default=b'Developer', max_length=15, choices=[(b'FULLSTACK', b'FullStack Developer'), (b'FRONTEND', b'Frontend Developer'), (b'ANDROID', b'Android Developer'), (b'DATA ANALYST', b'Data Analyst'), (b'IOS DEVELOPER', b'IOS Developer')]),
        ),
    ]
