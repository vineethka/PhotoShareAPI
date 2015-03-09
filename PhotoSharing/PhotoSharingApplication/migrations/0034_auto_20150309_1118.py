# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0033_auto_20150309_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 11, 18, 22, 816919)),
            preserve_default=True,
        ),
    ]
