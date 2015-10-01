# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_tagmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TagManager',
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborators',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
