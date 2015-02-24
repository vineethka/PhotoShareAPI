from django.conf.urls import patterns, url

from PhotoSharingApplication import api

urlpatterns = patterns('',
    url(r'^login', api.login, name='login'),
    url(r'^register', api.register, name='register'),

)