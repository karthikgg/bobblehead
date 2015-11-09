# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '__first__'),
        ('problems', '0002_remove_problem_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=None, max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('posted', models.DateField(auto_now_add=True)),
                ('problem', models.ForeignKey(default=None, to='problems.Problem')),
                ('user', models.ForeignKey(default=None, to='user_profile.UserProfile')),
            ],
        ),
    ]
