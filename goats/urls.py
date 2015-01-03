from django.conf.urls import patterns, url
from goats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.feed, name='feed'),
    url(r'^(?P<username>\w+)/goats/$', views.goatlist, name='goatlist'),
    url(r'^(?P<username>\w+)/goats/(?P<goat>\w+)/$', views.goat, name='goat'),
    url(r'^(?P<username>\w+)/event/$', views.event, name='event'),#event primary key?
)
