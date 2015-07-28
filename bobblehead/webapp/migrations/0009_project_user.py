# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_remove_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
