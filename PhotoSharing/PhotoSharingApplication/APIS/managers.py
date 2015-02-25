__author__ = 'suslov'
from django.contrib.auth.models import User, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, first_name=None, last_name=None):
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

        auth_user.save()
        current_user.save()

        return current_user