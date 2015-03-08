# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0003_auto_20150226_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturelikes',
            name='is_in_app_vote',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturelikes',
            name='like_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 9, 2, 56, 269924)),
            preserve_default=True,
        ),
    ]
