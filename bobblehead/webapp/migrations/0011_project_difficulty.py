# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20150805_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='difficulty',
            field=models.IntegerField(default=1, choices=[(b'EASY', 1), (b'MEDIUM', 2), (b'HARD', 3)]),
        ),
    ]
