# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0026_auto_20150308_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 1, 45, 41, 646017)),
            preserve_default=True,
        ),
    ]
