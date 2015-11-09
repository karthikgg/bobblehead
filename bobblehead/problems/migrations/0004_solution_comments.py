# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_remove_comment_submission'),
        ('problems', '0003_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='comments',
            field=models.ManyToManyField(to='comments.Comment'),
        ),
    ]
