# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import re
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('PhotoSharingApplication', '0017_auto_20150307_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=75, verbose_name='email address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', related_query_name='user', blank=True, related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=128, default='', verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_query_name='user', blank=True, related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=30, default='', help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username.', 'invalid')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 23, 46, 12, 778270)),
            preserve_default=True,
        ),
    ]
