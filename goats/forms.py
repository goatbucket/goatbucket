from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.forms.extras.widgets import SelectDateWidget
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

class EventModelForm(forms.ModelForm):
    class Meta:
        model = m.Event
        fields = '__all__'
        widgets = {'expiration': SelectDateWidget}

class HerdModelForm(forms.ModelForm):
    class Meta:
        model = m.Herd
        fields = ('name',)



#bulk entry form?
