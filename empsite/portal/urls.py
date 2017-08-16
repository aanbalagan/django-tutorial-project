from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<id>[0-9]+)/points$', views.points, name='points'),

]