from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

from PhotoSharingApplication.APIS.helpers.managers import UserProfileManager


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fb_user_id = models.CharField(max_length=100, blank=True)
    fb_access_token = models.CharField(max_length=100, blank=True)
    tw_user_id = models.CharField(max_length=100, blank=True)
    tw_access_token = models.CharField(max_length=100, blank=True)
    gp_user_id = models.CharField(max_length=100, blank=True)
    gp_access_token = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='uploaded_images/profile_pics')
    objects = UserProfileManager()

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def profile_image_src(self):
        return '<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.profile_image)
    profile_image_src.allow_tags = True

    def profile_image_link(self):
        return self.profile_image.url
    profile_image_link.allow_tags = True

    class Meta:
        db_table = "users"


class UserFriends(models.Model):
    user = models.ForeignKey(UserProfile)
    friend_id = models.CharField(max_length=30)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "user_friends"
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploaded_images/categories_pics')
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.name

    def image_src(self):
        return '<a href="/media/{0}"><img style="height:auto; width:auto; max-width:150px; max-height:150px;" src="/media/{0}"></a>'.\
            format(self.image)
    image_src.short_description = 'Preview'
    image_src.allow_tags = True

    def image_link(self):
        return self.image_link.url
    image_link.allow_tags = True

    class Meta:
        db_table = "categories"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Pictures(models.Model):
    category = models.ForeignKey(Categories)
    image = models.ImageField(upload_to='uploaded_images/pics')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    likes_count = models.IntegerField(max_length=9, default=0)

    def __unicode__(self):
        return self.name

    def thumb_image_src(self):
        return '<a href="/media/{0}"><img style="height:auto; width:auto; max-width:150px; max-height:150px;" src="/media/{0}"></a>'.\
            format(self.image)
    thumb_image_src.short_description = 'Preview'
    thumb_image_src.allow_tags = True

    def image_src(self):
        return '<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.image)
    image_src.allow_tags = True

    def image_link(self):
        return self.image_link.url
    image_link.allow_tags = True

    class Meta:
        db_table = "pictures"
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class PictureCategories(models.Model):
    category = models.ForeignKey(Categories)
    picture = models.ForeignKey(Pictures)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "picture_categories"
        verbose_name = 'Picture Category'
        verbose_name_plural = 'Picture Categories'


class PictureLikes(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "picture_likes"
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class PictureComments(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    commented_text = models.CharField(max_length=100)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "picture_comments"
        verbose_name = 'Comment'
        verbose_name_plural = 'Picture Comments'


class UserActivation(models.Model):
    user = models.ForeignKey(UserProfile)
    authentication_key = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "user_activation"




