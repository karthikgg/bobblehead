# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nanodegree', models.CharField(max_length=15, choices=[(b'FULLSTACK', b'FullStack Developer'), (b'FRONTEND', b'Frontend Developer'), (b'ANDROID', b'Android Developer'), (b'DATA ANALYST', b'Data Analyst'), (b'IOS DEVELOPER', b'IOS Developer')])),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='project_category',
            new_name='tag_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(default=b'STUDENT', max_length=15, choices=[(b'STUDENT', b'Student Project'), (b'UDACITY', b'Udacity Project'), (b'ENTERPRISE', b'Enterprise Project'), (b'OPEN SOURCE', b'Open Source'), (b'CONTEST', b'Contest')]),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='userproject',
            name='project',
            field=models.ForeignKey(to='webapp.Project'),
        ),
        migrations.AddField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(to='webapp.User'),
        ),
        migrations.AddField(
            model_name='tagsproject',
            name='project',
            field=models.ForeignKey(to='webapp.Project'),
        ),
        migrations.AddField(
            model_name='tagsproject',
            name='tag',
            field=models.ForeignKey(to='webapp.Tag'),
        ),
    ]
