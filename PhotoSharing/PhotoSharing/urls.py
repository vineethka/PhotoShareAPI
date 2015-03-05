from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="home"),
)
from django.contrib import admin

admin.site.site_header = 'Farpic administration'
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PhotoSharing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('PhotoSharingApplication.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='templates/robots.txt'), name='robots.txt', mimetype='text/plain'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
