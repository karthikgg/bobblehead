# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_project_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='difficulty',
            field=models.IntegerField(default=1, choices=[(b'EASY', b'Easy'), (b'MEDIUM', b'Medium'), (b'HARD', b'Hard')]),
        ),
    ]
