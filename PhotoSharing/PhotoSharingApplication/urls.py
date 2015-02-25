from django.conf.urls import patterns, url

from PhotoSharingApplication.APIS import user_manager_api, categories_api_manager

urlpatterns = patterns('',
    url(r'^login', user_manager_api.login, name='login'),
    url(r'^register', user_manager_api.register, name='register'),
    url(r'^get_all_categories', categories_api_manager.get_all_categories, name='get_all_categories'),


)