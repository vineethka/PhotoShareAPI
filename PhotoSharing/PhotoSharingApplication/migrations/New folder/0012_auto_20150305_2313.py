# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0011_auto_20150304_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 23, 13, 18, 282413)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pictures',
            name='category',
            field=models.ForeignKey(to='PhotoSharingApplication.Categories', blank=True),
            preserve_default=True,
        ),
    ]
