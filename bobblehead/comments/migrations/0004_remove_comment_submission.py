# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20151109_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='submission',
        ),
    ]
