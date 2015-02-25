from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.site.site_header = 'Photo Share administration'
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PhotoSharing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photoshare/', include('PhotoSharingApplication.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
