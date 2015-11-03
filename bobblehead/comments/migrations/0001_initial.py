# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '__first__'),
        ('user_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('sub', models.ForeignKey(default=None, to='submissions.Submission')),
                ('user', models.ForeignKey(default=None, to='user_profile.UserProfile')),
            ],
        ),
    ]
