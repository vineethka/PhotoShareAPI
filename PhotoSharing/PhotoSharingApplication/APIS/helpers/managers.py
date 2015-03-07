__author__ = 'suslov'
from django.contrib.auth.models import User, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, first_name=None, last_name=None, dob=None):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not username:
            raise ValueError('Users must have a valid username.')

        auth_user = User.objects.create_user(username, email, password)
        auth_user.first_name = first_name
        auth_user.last_name = last_name
        current_user = self.model(
            user=auth_user,
        )
        if dob:
            current_user.dob = dob
        current_user.save()
        auth_user.save()

        return current_user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

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
