# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nanodegree', models.CharField(max_length=15, choices=[(b'FULLSTACK', b'FullStack Developer'), (b'FRONTEND', b'Frontend Developer'), (b'ANDROID', b'Android Developer'), (b'DATA ANALYST', b'Data Analyst'), (b'IOS DEVELOPER', b'IOS Developer')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
