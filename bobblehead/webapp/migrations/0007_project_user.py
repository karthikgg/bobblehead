# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0006_remove_project_user'),
    ]

    # operations = [
    #     migrations.AddField(
    #         model_name='project',
    #         name='user',
    #         field=models.OneToOneField(default=datetime.datetime(2015, 7, 23, 1, 13, 13, 830843, tzinfo=utc), to=settings.AUTH_USER_MODEL),
    #         preserve_default=False,
    #     ),
    # ]
