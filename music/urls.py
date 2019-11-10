from django.conf.urls import url
from . import views


urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/712 (here 712 is the id of the album we want to open
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
