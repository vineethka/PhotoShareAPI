# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0012_auto_20150305_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 23, 22, 54, 595948)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pictures',
            name='description',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pictures',
            name='name',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
