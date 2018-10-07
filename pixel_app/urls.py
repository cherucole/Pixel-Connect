from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[


    url(r'^$', views.homepage, name='homepage'),
    # url(r'^post/(?P<id>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^post/(?P<id>\d+)/like/$', views.like_post, name='like_post'),
    url(r'^upload$', views.upload_image, name='upload'),
    #

    url(r'^accounts/profile/', views.my_profile, name='my_profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),

    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    # url(r'^leave_comment/(?P<pk>\d+)', views.leave_comment, name='leave_comment'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)