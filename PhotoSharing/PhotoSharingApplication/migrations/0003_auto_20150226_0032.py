# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0002_auto_20150225_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='user',
            field=models.ForeignKey(default=1, to='PhotoSharingApplication.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 0, 31, 25, 916394)),
            preserve_default=True,
        ),
    ]
