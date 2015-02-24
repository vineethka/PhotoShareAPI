from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user = models.OneToOneField(User)
    fb_user_id = models.CharField(max_length=100, blank=True)
    fb_access_token = models.CharField(max_length=100, blank=True)
    tw_user_id = models.CharField(max_length=100, blank=True)
    tw_access_token = models.CharField(max_length=100, blank=True)
    gp_user_id = models.CharField(max_length=100, blank=True)
    gp_access_token = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics')

    class Meta:
        db_table = "users"


class UserFriends(models.Model):
    user = models.ForeignKey(Users)
    friend_id = models.CharField(max_length=30)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "user_friends"
        verbose_name = 'User_Friend'
        verbose_name_plural = 'user_friends'


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories_pics')
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "categories"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Pictures(models.Model):
    category = models.ForeignKey(Categories)
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    likes_count = models.IntegerField(max_length=9, default=0)

    class Meta:
        db_table = "pictures"


class PictureCategories(models.Model):
    category = models.ForeignKey(Categories)
    picture = models.ForeignKey(Pictures)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "picture_categories"


class PictureLikes(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(Users)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "picture_likes"


class PictureComments(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(Users)
    commented_text = models.CharField(max_length=100)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "picture_comments"


class UserActivation(models.Model):
    user = models.ForeignKey(Users)
    authentication_key = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "user_activation"




