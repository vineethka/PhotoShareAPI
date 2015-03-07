from django.contrib.auth.backends import ModelBackend
from PhotoSharingApplication.models import UserProfile


class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None):
        try:
            return UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None