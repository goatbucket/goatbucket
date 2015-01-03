from django.http import HttpResponse
from django.template import RequestContext, loader

from goats.models import Event, Goat, Herd, UserProfile


def index(request):
    return HttpResponse("Hello, world. You're at the goats index.")
    
def feed(request, username):
    kwargs = {}
    kwargs['feed_display'] = True
    kwargs['goat__herd__user__username'] = username
    event_list = Event.objects.filter(**kwargs).order_by('-expiration').distinct()
    template = loader.get_template('goats/feed.html')
    context = RequestContext(request, {'event_list': event_list})
    return HttpResponse(template.render(context))
    
def hide(request, username):
    event = Event.objects.get(pk=request.POST['event'])
    event.feed_display = False
    event.save()
    return HttpResponseRedirect(reverse('views.feed', args=(username)))
    
def goatlist(request, username):
    kwargs = {}
    kwargs['herd__user__username'] = username
    goat_list = Goat.objects.filter(**kwargs).distinct()
    template = loader.get_template('goats/goatlist.html')
    context = RequestContext(request, {'goat_list': goat_list})
    return HttpResponse(template.render(context))
    
def goat(request, username, goat):
    goat = Goat.objects.get(name = goat)
    template = loader.get_template('goats/goat.html')
    context = RequestContext(request, {'goat': goat})
    return HttpResponse(template.render(context))
    
def event(request, username):
    return HttpResponse("event")    

