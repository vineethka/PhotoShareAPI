from django.conf.urls import patterns, url

from PhotoSharingApplication import views

urlpatterns = patterns('',
    url(r'^login', views.login, name='login'),
)