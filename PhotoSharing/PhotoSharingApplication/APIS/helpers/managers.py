from django.utils import timezone

__author__ = 'suslov'
from django.contrib.auth.models import User, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)


    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = UserProfileManager.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=False, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                 **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


    @staticmethod
    def create_facebook_user(self, user_id, access_token=None, email=None, first_name=None, last_name=None):
        if not access_token:
            raise ValueError("Users must have access token")

        if not email:
            raise ValueError("Users must have a valid email address")

        if not user_id:
            raise ValueError("Users must have a valid user id")

        auth_user = User.objects.create_user(user_id, email)
        password = User.objects.make_random_password()
        auth_user.set_password(password)
        auth_user.first_name = first_name
        auth_user.last_name = last_name

        current_user = self.model(
            user=auth_user,
            fb_user_id=user_id,
            fb_access_token=access_token,
        )

        auth_user.save()
        current_user.save()
        return current_user
