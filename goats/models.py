from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from simple_history.models import HistoricalRecords
from datetime import *
from swingtime import models as swingtime

#Contains a user's Goats.
class Herd(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    history = HistoricalRecords()

#Basic information for the users' animals - not necessarily goats.
class Goat(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    dam = models.ForeignKey("self", related_name="mammy", null = True, blank = True)
    sire = models.ForeignKey("self", related_name="pappy", null = True, blank = True)
    sex_choices = (('F','Doe'), ('M','Buck'), ('X','Intersex'))
    sex = models.CharField(max_length=1, choices=sex_choices)
    birthday = models.DateTimeField(null = True, blank = True) #want to be able to accept partial data
    birthweight = models.FloatField(null = True, blank = True)
    breed = models.CharField(max_length=30, blank = True, default='')
    coat = models.CharField(max_length=30, blank = True, default='')
    ears = models.CharField(max_length=30, blank = True, default='')
    nickname = models.CharField(max_length=30, blank = True, default='')
    status_choices = (('A','Active'), ('R','Retired'), ('D','Dead'), ('S','Sold'))
    status = models.CharField(max_length=1, choices=status_choices, null = True)
    herd = models.ForeignKey(Herd, null = True, blank = True)
    weight = models.FloatField(null = True, blank = True)
    tag = models.CharField(max_length=30, null = True, blank = True)
    notes = models.CharField(max_length=300, null = True, blank = True)
    history = HistoricalRecords()
    alerts = models.ManyToManyField(swingtime.Occurrence, null = True, blank = True)

#an additional model that holds any certifications an animal has.   
class GoatRegistration(models.Model):
    goat = models.ForeignKey(Goat)
    registration = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    #??????Awards??????


#The purpose of reminders is to prompt the user to record data, and to keep track of herd management activities for them. 


class Picture(models.Model):
    goat = models.ManyToManyField(Goat) # manytomany for multigoat pictures? Picture can also be linked to herd?
    url = models.CharField(max_length=30)

class GoatEvent(swingtime.Event):
    user = models.ForeignKey(User)
    
