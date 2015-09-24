# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20150901_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='tagsproject',
            name='project',
        ),
        migrations.RemoveField(
            model_name='tagsproject',
            name='tag',
        ),
        migrations.DeleteModel(
            name='TagsProject',
        ),
    ]
