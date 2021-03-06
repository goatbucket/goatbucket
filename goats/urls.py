from django.conf.urls import patterns, url
from goats import views
from goatbucket.models import Goat, Herd 
from django_filters.views import FilterView

urlpatterns = patterns('',
     #displays splash with login or redirects to /username
    url(r'^$', views.index, name='index'),

    #form to create new object
    url(r'^new/(?P<url_object>goat|herd|alert)/$', views.new, name='new'),

    #stat page and history for goats, with editable fields
    #this needs a detail view with a post and a get.
    #might want to reference by an ID number rather than name/
    url(r'^goat/(?P<name>\w+)/$', views.detail, name='detail'),

    #lists all objects, or objects that match optional search
    #optional search is not functional right now
    #can I make the name include the object?
    url(r'^herd/$', FilterView.as_view(model = Herd), name='herdlist'),

    url(r'^goat/$', views.goatlist, name='goatlist'),

    #shows upcoming events
    url(r'^(?P<username>\w+)/$', views.feed, name='feed'),

    #list of goats in herd
    #this is the above but search herd=herdname?
    #url(r'^/herd/(?P<name>\w+)/$', views.object_list, name='object_list'),

    #/data/new/<parameters> : (??) a form to upload data for multiple goats
    #/data/view : (???) analytics
)
