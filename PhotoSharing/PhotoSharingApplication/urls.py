from django.conf.urls import patterns, url

from PhotoSharingApplication.APIS import user_manager_api, categories_api_manager, picture_manager_api
from PhotoSharingApplication import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^do_login', user_manager_api.do_login, name='do_login'),
    url(r'^do_logout', user_manager_api.do_logout, name='do_logout'),
    url(r'^do_register', user_manager_api.do_register, name='do_register'),
    url(r'^upload_profile_image', user_manager_api.upload_profile_image, name='upload_profile_image'),
    url(r'^do_contact_us', user_manager_api.do_contact_us, name='do_contact_us'),

    url(r'^login', views.login, name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^register', views.register, name='register'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^category_list', views.category_list, name='category_list'),
    url(r'^category/(?P<category_id>\d+)', views.category_detail, name="category_detail"),
    url(r'^likes', views.likes, name="likes"),
    url(r'^uploaded', views.uploaded, name="uploaded"),
    url(r'^report_a_pic/(?P<picture_id>\d+)', views.report_a_pic, name="report_a_pic"),
    url(r'^image_details/(?P<picture_id>\d+)', views.image_details, name="image_details"),
    url(r'^abuse_picture', picture_manager_api.abuse_picture, name='abuse_picture'),
    url(r'^upload_picture', picture_manager_api.upload_picture, name='upload_picture'),
    url(r'^upload', views.upload, name="upload"),
    url(r'^contact_us', views.contact_us, name="contact_us"),
    url(r'^popular_pics', views.popular_pics, name="popular_pics"),
    url(r'^help', views.help, name="help"),


    url(r'^facebooklogin', user_manager_api.facebook_login, name='facebooklogin'),
    url(r'^get_all_categories', categories_api_manager.get_all_categories, name='get_all_categories'),
    url(r'^get_pictures_for_category', categories_api_manager.get_pictures_for_category, name='get_pictures_for_category'),
    url(r'^like', picture_manager_api.like, name='like'),
    url(r'^abuse_picture', picture_manager_api.abuse_picture, name='abuse_picture'),


)