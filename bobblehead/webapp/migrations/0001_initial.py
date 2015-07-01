# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('collaborators', models.IntegerField(default=1)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('category', models.CharField(default=b'STUDENT', max_length=15, choices=[(b'STUDENT', b'Student Project'), (b'UDACITY', b'Udatcity Project'), (b'ENTERPRISE', b'Enterprise Project'), (b'OPEN SOURCE', b'Open Source'), (b'CONTEST', b'Contest')])),
                ('articles', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('udcaity_student', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ForeignKey(to='webapp.Tags'),
        ),
    ]
