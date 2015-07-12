from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from registration.forms import RegistrationForm

import django_filters

from goats import models as m

class HerdRegistrationForm(RegistrationForm):
    herd = forms.CharField(max_length=30)
    class Meta:
        fields = ('herd')

class GoatModelForm(forms.ModelForm):
    class Meta:
        model = m.Goat
        fields = '__all__'
        widgets = {'birthday': SelectDateWidget}

class HerdModelForm(forms.ModelForm):
    class Meta:
        model = m.Herd
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class GoatFilter(django_filters.FilterSet):
    class Meta:
        model = m.Goat
        fields = ['name']



#bulk entry form?
