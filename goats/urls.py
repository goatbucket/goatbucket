from django.conf.urls import patterns, url
from goats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^goats/new$', views.new_goat, name='goat'),
    url(r'^herds/new$', views.new_herd, name='herd'),
    url(r'^events/new$', views.new_event, name='event'),
    url(r'^(?P<username>\w+)/$', views.feed, name='feed'),
    #url(r'^(?P<username>\w+)/goats/$', views.goatlist, name='goatlist'),
    #url(r'^(?P<username>\w+)/goats/(?P<goat>\w+)/$', views.goat, name='goat'),
    #url(r'^(?P<username>\w+)/event/$', views.event, name='event'),#event primary key? 
)
