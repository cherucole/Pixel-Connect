from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[


    url(r'^$', views.homepage, name='homepage'),
    url(r'^post/(?P<id>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^post/(?P<id>\d+)/like/$', views.like_post, name='like_post'),
    url(r'^upload$', views.upload_image, name='upload'),
    #

    url(r'^accounts/profile/', views.my_profile, name='my_profile'),
    url(r'^search/', views.search, name='search'),
url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),

    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^comment/', views.new_comment, name='add_comments'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),


    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^location/', views.my_locations, name='location_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)