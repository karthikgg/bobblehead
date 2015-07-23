# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_project_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproject',
            name='project',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserProject',
        ),
    ]
