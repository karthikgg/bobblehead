# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20150901_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='difficulty',
            field=models.CharField(default=1, max_length=10, choices=[(b'EASY', b'Easy'), (b'MEDIUM', b'Medium'), (b'HARD', b'Hard')]),
        ),
    ]
