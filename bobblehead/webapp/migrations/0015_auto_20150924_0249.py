# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20150922_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='articles',
        ),
        migrations.AddField(
            model_name='project',
            name='articles',
            field=models.ManyToManyField(to='webapp.Articles'),
        ),
    ]
