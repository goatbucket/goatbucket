from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

import string

from swingtime import models as swingtime
from models import *
from goats import forms as f

from datetime import *
from swingtime import models as swingtime

#returns landing/login page or redirect
def index(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect(reverse(feed, args=[request.user.username]))
    return HttpResponseRedirect('accounts/login')

#newsfeed page, would be great if I could fit with object list
@login_required
def feed(request, username):
    if request.user.username == username:
        kwargs = {}
        kwargs['goat__herd__user'] = request.user.id
        alert_list = swingtime.Occurrence.objects.filter(**kwargs).order_by('start_time')
        #group similar events with OccurrenceManager.dailyoccurrences()
        template = loader.get_template('goats/feed.html')
        context = RequestContext(request, {'alert_list': alert_list})
        return HttpResponse(template.render(context))
    return HttpResponse("these aren't your goats!")#really should be an 404 page

@login_required
def goatlist(request):
    kwargs = {}
    kwargs['herd__user'] = request.user.id
    goat_list = f.GoatFilter(request.GET, queryset=Goat.objects.filter(**kwargs))
    template = loader.get_template('goats/goat_filter.html')
    context = RequestContext(request, {'goat_list': goat_list})
    return HttpResponse(template.render(context))

@login_required
def detail(request, name):
    return HttpResponse("you're looking at a goat")


#creates a new instance of an object
@login_required
def new(request, user, url_object):
    form_title = string.capitalize(url_object)
    form = eval('f.' + form_title + 'ModelForm()')
    if request.method == 'POST':
        form = eval('f.' + form_title + 'ModelForm(request.POST)')
        if form.user:
            form.user = user
        if form.is_valid():
            new_object = form.cleaned_data.save()
            return render(request, 'goats/submission_form.html', 
                {'form': form, 'form_title': form_title, 'message': 'success!'})
        return render(request, 'goats/submission_form.html', 
            {'form': form, 'form_title': form_title, 'message': 'there was an error!'})
    return render(request, 'goats/submission_form.html',
        {'form': form, 'form_title': form_title})

#updates an instance of an object

