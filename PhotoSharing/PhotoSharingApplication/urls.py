from django.conf.urls import patterns, url
from PhotoSharingApplication.APIS import user_manager_api


urlpatterns = patterns('',
    url(r'^login', user_manager_api.login, name='login'),
    url(r'^register', user_manager_api.register, name='register'),
    url(r'^facebooklogin', user_manager_api.facebook_login, name='facebooklogin'),
)