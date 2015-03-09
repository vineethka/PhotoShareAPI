from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from PhotoSharingApplication.APIS.helpers.managers import UserProfileManager
import re
import uuid
from django.core import validators
from django.utils import timezone


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30, default='')
    last_name = models.CharField(_('last name'), max_length=30, default='')
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    fb_user_id = models.CharField(max_length=100, blank=True)
    fb_access_token = models.CharField(max_length=100, blank=True)
    tw_user_id = models.CharField(max_length=100, blank=True)
    tw_access_token = models.CharField(max_length=100, blank=True)
    gp_user_id = models.CharField(max_length=100, blank=True)
    gp_access_token = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='uploaded_images/profile_pics')
    power_votes = models.IntegerField(default=0)
    ad_enabled = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __unicode__(self):
        return u"%s" % self.get_full_name()

    def __str__(self):
        return "%s" % self.get_full_name()

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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_authenticated(self):
        return True

    class Meta:
        db_table = "users"
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserFriends(models.Model):
    user = models.ForeignKey(UserProfile)
    friend_id = models.CharField(max_length=30)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    class Meta:
        db_table = "user_friends"
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploaded_images/categories_pics')
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return "%s" % self.name

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
    category = models.ForeignKey(Categories, blank=True)
    user = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to='uploaded_images/pics')
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)
    likes_count = models.IntegerField(max_length=9, default=0)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return "%s" % self.name

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

# only needed in future
class PictureCategories(models.Model):
    category = models.ForeignKey(Categories)
    picture = models.ForeignKey(Pictures)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    class Meta:
        db_table = "picture_categories"
        verbose_name = 'Picture Category'
        verbose_name_plural = 'Picture Categories'


class PictureLikes(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    like_count = models.IntegerField(default=0)
    is_in_app_vote = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    class Meta:
        db_table = "picture_likes"
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class PictureComments(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    commented_text = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.commented_text

    def __str__(self):
        return "%s" % self.commented_text

    class Meta:
        db_table = "picture_comments"
        verbose_name = 'Picture Comment'
        verbose_name_plural = 'Picture Comments'


class UserActivation(models.Model):
    user = models.ForeignKey(UserProfile)
    authentication_key = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "user_activation"


class PictureAbuseReports(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    subject = models.CharField(max_length=150, blank=True)
    comment = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.comment

    def __str__(self):
        return "%s" % self.comment

    class Meta:
        db_table = "picture_abuse_reports"
        verbose_name = 'User Reported Issue'
        verbose_name_plural = 'User Reported Issues'


class ContactUs(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150, blank=True)
    comment = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s" % self.subject

    def __str__(self):
        return "%s" % self.subject

    class Meta:
        db_table = "contact_us"
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class Contest(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    start_at = models.DateTimeField(default=datetime.now)
    end_at = models.DateTimeField(default=datetime.now()+timedelta(days=14))
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "contest"
        verbose_name = 'Contest'
        verbose_name_plural = 'Contests'


class ContestVotes(models.Model):
    picture = models.ForeignKey(Pictures)
    user = models.ForeignKey(UserProfile)
    contest = models.ForeignKey(Contest)
    updated_at = models.DateTimeField(default=datetime.now, auto_now=True)
    created_at = models.DateTimeField(default=datetime.now, auto_now_add=True)

    class Meta:
        db_table = "contest_votes"
        verbose_name = 'Contest Vote'
        verbose_name_plural = 'Contest Votes'



class ContestReward(models.Model):
    contest = models.ForeignKey(Contest)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploaded_images/rewards')

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "contest_reward"
        verbose_name = 'Contest Reward'
        verbose_name_plural = 'Contest Reward'


class ContestWinners(models.Model):
    contest = models.ForeignKey(Contest)
    user = models.ForeignKey(UserProfile)
    picture = models.ForeignKey(Pictures)
    contest_reward = models.ForeignKey(ContestReward)
    comment = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return u"%s" % self.user

    def __str__(self):
        return "%s" % self.user

    class Meta:
        db_table = "contest_winners"
        verbose_name = 'Contest Winner'
        verbose_name_plural = 'Contest Winners'
