from django.contrib.auth import authenticate
from PhotoSharingApplication.models import UserProfile


def login_authenticate(request):
    user_email = request.data['email']
    user_password = request.data['password']

    try:
        user = UserProfile.objects.get(email=user_email)
        if user.check_password(user_password):
            return user
    except UserProfile.DoesNotExist:
        return None


def authenticate(request):
    user_name = request.data['user']
    user_password = request.data['password']
    user = UserProfile.objects.get(username=user_name)
    if user is not None:
        if user.password == user_password:
            return user
        else:
            return None
    else:
        # the authentication system was unable to verify the username and password
        return None


def get_user_with_email_address(email):
    try:
        user = UserProfile.objects.get(email=email)
        if user is not None:
            return user
        else:
            return None
    except UserProfile.DoesNotExist:
        return None

def get_user_with_username(username):
    try:
        user = UserProfile.objects.get(username=username)
        if user is not None:
            return user
        else:
            return None
    except UserProfile.DoesNotExist:
        return None