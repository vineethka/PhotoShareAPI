# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoSharingApplication', '0032_auto_20150309_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 8, 12, 26, 214796)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')]),
            preserve_default=True,
        ),
    ]
