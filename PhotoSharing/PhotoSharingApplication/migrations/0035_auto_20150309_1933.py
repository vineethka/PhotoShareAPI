# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0034_auto_20150309_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 19, 33, 30, 849000)),
            preserve_default=True,
        ),
    ]
