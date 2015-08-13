# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_remove_userprofile_user'),
        ('webapp', '0010_auto_20150805_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(to='user_profile.UserProfile')),
                ('project', models.ForeignKey(to='webapp.Project')),
            ],
        ),
    ]
