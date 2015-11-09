# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20151109_1031'),
        ('projects', '__first__'),
        ('user_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('posted', models.DateField(auto_now_add=True)),
                ('category', models.CharField(default=b'CHALLENGE', max_length=15, choices=[(b'INTERVIEW', b'Interview Problem'), (b'CHALLENGE', b'Challenge Problem'), (b'QUESTION', b'The "I-have-a" Problem'), (b'CONTEST', b'Contest')])),
                ('difficulty', models.CharField(default=1, max_length=10, choices=[(b'EASY', b'Easy'), (b'MEDIUM', b'Medium'), (b'HARD', b'Hard')])),
                ('link', models.URLField(default=None, max_length=500)),
                ('questions', models.ManyToManyField(to='comments.Question')),
                ('tags', models.ManyToManyField(to='projects.Tag')),
                ('user', models.ForeignKey(default=None, to='user_profile.UserProfile')),
            ],
        ),
    ]
