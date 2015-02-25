from django.conf.urls import patterns, url

from PhotoSharingApplication.APIS import user_manager_api, categories_api_manager

urlpatterns = patterns('',
    url(r'^login', user_manager_api.login, name='login'),
    url(r'^register', user_manager_api.register, name='register'),
<<<<<<< HEAD
    url(r'^facebooklogin', user_manager_api.facebook_login, name='facebooklogin'),
=======
    url(r'^get_all_categories', categories_api_manager.get_all_categories, name='get_all_categories'),
    url(r'^get_pictures_for_category', categories_api_manager.get_pictures_for_category, name='get_pictures_for_category'),


>>>>>>> 84256a1285ce2c02be555dec9d106adc839b3b58
)