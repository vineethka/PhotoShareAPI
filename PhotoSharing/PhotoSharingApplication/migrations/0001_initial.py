# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploaded_images/categories_pics')),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'categories',
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=150, blank=True)),
                ('comment', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'contact_us',
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_at', models.DateTimeField(default=datetime.datetime.now)),
                ('end_at', models.DateTimeField(default=datetime.datetime(2015, 3, 11, 22, 3, 12, 652554))),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'contest',
                'verbose_name': 'Contest',
                'verbose_name_plural': 'Contests',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContestReward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('amount', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='uploaded_images/rewards')),
                ('contest', models.ForeignKey(to='PhotoSharingApplication.Contest')),
            ],
            options={
                'db_table': 'contest_reward',
                'verbose_name': 'Contest Reward',
                'verbose_name_plural': 'Contest Reward',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContestVotes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
                ('contest', models.ForeignKey(to='PhotoSharingApplication.Contest')),
            ],
            options={
                'db_table': 'contest_votes',
                'verbose_name': 'Contest Vote',
                'verbose_name_plural': 'Contest Votes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContestWinners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment', models.CharField(max_length=200, blank=True)),
                ('contest', models.ForeignKey(to='PhotoSharingApplication.Contest')),
                ('contest_reward', models.ForeignKey(to='PhotoSharingApplication.ContestReward')),
            ],
            options={
                'db_table': 'contest_winners',
                'verbose_name': 'Contest Winner',
                'verbose_name_plural': 'Contest Winners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAbuseReports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=150, blank=True)),
                ('comment', models.CharField(max_length=1000)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'picture_abuse_reports',
                'verbose_name': 'User Reported Issue',
                'verbose_name_plural': 'User Reported Issues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(to='PhotoSharingApplication.Categories')),
            ],
            options={
                'db_table': 'picture_categories',
                'verbose_name': 'Picture Category',
                'verbose_name_plural': 'Picture Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('commented_text', models.CharField(max_length=100, blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'picture_comments',
                'verbose_name': 'Picture Comment',
                'verbose_name_plural': 'Picture Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'picture_likes',
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='uploaded_images/pics')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
                ('likes_count', models.IntegerField(default=0, max_length=9)),
                ('category', models.ForeignKey(to='PhotoSharingApplication.Categories')),
            ],
            options={
                'db_table': 'pictures',
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('authentication_key', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_activation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFriends',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('friend_id', models.CharField(max_length=30)),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'user_friends',
                'verbose_name': 'Friend',
                'verbose_name_plural': 'Friends',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fb_user_id', models.CharField(max_length=100, blank=True)),
                ('fb_access_token', models.CharField(max_length=100, blank=True)),
                ('tw_user_id', models.CharField(max_length=100, blank=True)),
                ('tw_access_token', models.CharField(max_length=100, blank=True)),
                ('gp_user_id', models.CharField(max_length=100, blank=True)),
                ('gp_access_token', models.CharField(max_length=100, blank=True)),
                ('profile_image', models.ImageField(upload_to='uploaded_images/profile_pics')),
                ('power_votes', models.IntegerField(default=0)),
                ('ad_enabled', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userfriends',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useractivation',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturelikes',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturelikes',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturecomments',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturecomments',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturecategories',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pictureabusereports',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pictureabusereports',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contestwinners',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contestwinners',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contestvotes',
            name='picture',
            field=models.ForeignKey(to='PhotoSharingApplication.Pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contestvotes',
            name='user',
            field=models.ForeignKey(to='PhotoSharingApplication.UserProfile'),
            preserve_default=True,
        ),
    ]
