# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_remove_userprofile_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set([('email', 'nickname')]),
        ),
    ]
