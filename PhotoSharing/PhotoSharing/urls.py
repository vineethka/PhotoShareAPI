from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PhotoSharing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('PhotoSharingApplication.urls')),
)
