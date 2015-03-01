# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0004_auto_20150226_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 11, 28, 59, 48492)),
            preserve_default=True,
        ),
    ]
