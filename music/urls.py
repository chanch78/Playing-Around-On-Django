from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/id_pk/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/id_pk/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/id_pk/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    #/music/id_pk/favorite/
    #url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]