# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_solution_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='description',
            field=models.TextField(),
        ),
    ]
