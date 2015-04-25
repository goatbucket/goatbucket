from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from goats.models import Event, Goat, Herd
from goats import forms as f

from registration.backends.simple.views import RegistrationView


def index(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect(reverse(feed, args=[request.user.username]))
    return HttpResponseRedirect('accounts/login')

@login_required
def feed(request, username):
    kwargs = {}
    kwargs['feed_display'] = True
    kwargs['goat__herd__user'] = request.user.id
    event_list = Event.objects.filter(**kwargs).order_by('-expiration').distinct()
    template = loader.get_template('goats/feed.html')
    context = RequestContext(request, {'event_list': event_list})
    return HttpResponse(template.render(context))

@login_required
def new_goat(request):
    form_title = 'Goat'
    if request.method == 'POST':
        form = f.GoatModelForm(request.POST)
        if form.is_valid():
            new_goat = form.save()
            return HttpResponseRedirect("/")
        return render(request, 'goats/submission_form.html', {'form': form, 'form_title': form_title})
    form = f.GoatModelForm()
    return render(request, 'goats/submission_form.html',{'form': form, 'form_title': form_title}) 

@login_required
def new_herd(request):
    form_title = 'Herd'
    if request.method == 'POST':
        form = f.HerdModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user = request.user
            herd = Herd.objects.create(name=name, user=user)
            return HttpResponseRedirect("/goats/new")
        return render(request, 'goats/submission_form.html', {'form': form, 'form_title': form_title})
    form = f.HerdModelForm()
    return render(request, 'goats/submission_form.html',{'form': form, 'form_title': form_title}) 

@login_required
def new_event(request):
    form_title = 'Event'
    if request.method == 'POST':
        form = f.EventModelForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            return HttpResponseRedirect("/")
        return render(request, 'goats/submission_form.html', {'form': form, 'form_title': form_title})
    form = f.EventModelForm()
    return render(request, 'goats/submission_form.html',{'form': form, 'form_title': form_title})


class MyRegistrationView(RegistrationView):
    def success_url(self, request, user):
        return "/view_is_decider"



