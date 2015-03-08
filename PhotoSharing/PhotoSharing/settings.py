"""
Django settings for PhotoSharing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings
from PhotoSharing.config import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'exn@x3i9yc+uno+q9^mqu8xmecrt9pmioy0d&89hh23(tx%=ij'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PhotoSharingApplication',
    'rest_framework',
    'social.apps.django_app.default',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'PhotoSharingApplication.disable.DisableCSRF',

    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',

)


AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'PhotoSharingApplication.auth_backend.PasswordlessAuthBackend',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',

    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

ROOT_URLCONF = 'PhotoSharing.urls'

WSGI_APPLICATION = 'PhotoSharing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'photoshare',
        'USER': 'root',
        'PASSWORD': 'qburst',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GRAPPELLI_ADMIN_TITLE = "Farpic Application"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-filesF/

STATIC_URL = '/static/'

# TODO: need to verify these values before release
MEDIA_URL = '/media/'
MEDIA_ROOT = ''
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')


GRAPPELLI_INDEX_DASHBOARD = 'PhotoSharing.dashboardhelper.CustomIndexDashboard'
# GRAPPELLI_INDEX_DASHBOARD = {  # alternative method
#     'PhotoSharing.admin.admin_site': 'PhotoSharing.my_dashboard.CustomIndexDashboard',
# }
## Also add this at the bottom of the fille:
AUTH_USER_MODEL = 'PhotoSharingApplication.UserProfile'
# SOCIAL_AUTH_USER_MODEL = 'PhotoSharingApplication.UserProfile'
# LOGIN_REDIRECT_URL = '/'





