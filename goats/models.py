from django.db import models
from django.contrib.auth.models import User

class Herd(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

class Goat(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank = True)
    status_choices = (('A','Active'), ('D','Dead'), ('S','Sold'))
    status = models.CharField(max_length=1, choices=status_choices, null = True)
    dam = models.ForeignKey("self", related_name="mammy", null = True, blank = True)
    sire = models.ForeignKey("self", related_name="pappy", null = True, blank = True)
    sex_choices = (('F','Doe'), ('M','Buck'), ('X','Intersex'))
    sex = models.CharField(max_length=1, choices=sex_choices, null = True) 
    herd = models.ForeignKey(Herd, null = True, blank = True)
    birthweight = models.FloatField(null = True, blank = True)
    weight = models.FloatField(null = True, blank = True)
    birthday = models.DateTimeField(null = True, blank = True) #want to be able to accept partial data - just the year or m/y
    tag = models.CharField(max_length=30, null = True, blank = True)
    notes = models.CharField(max_length=300, null = True, blank = True)
    breed = models.CharField(max_length=30, null = True, blank = True)
    coat = models.CharField(max_length=30, null = True, blank = True)
    ears = models.CharField(max_length=30, null = True, blank = True)

class GoatRegistration(models.Model):
    goat = models.ForeignKey(Goat)
    registration = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    #??????Awards??????

#ask about class inheritance/composition for related events.
class Event(models.Model):
    def __str__(self):
        notes = self.notes
        goats = ', '.join([goat.name for goat in self.goat.all()])
        return goats +': '+ notes
    def event_notes(self):
        #TODO: rounds up notes and health_type information and formats it somehow.
        pass
    date = models.DateTimeField()
    expiration = models.DateTimeField()
    status_choices = (('A','Active'), ('D','Dead'), ('S','Sold'))
    goat_status = models.CharField(max_length=1, choices=status_choices, null = True)
    event_choices = (
    ('B','Birth'), ('H','Health'), ('D','Death'), ('T','Purchase/Sale'),
    ('M','New Milk Record'), ('L','New Lactation'))
    event_type = models.CharField(max_length=1, choices=event_choices, null = True)
    feed_display = models.BooleanField(default=True)
    goat = models.ManyToManyField(Goat)
    notes = models.CharField(max_length=300)

class BirthEvent(models.Model):
    event  = models.ForeignKey(Event)
    kids = models.ManyToManyField(Goat)
    def __str__(self):
        return str(self.event.date)

class HealthEvent(models.Model):
    def __str__(self):
        return self.health_type
    event  = models.ForeignKey(Event)
    health_type = models.CharField(max_length=30)

class TransactionEvent(models.Model): 
    event  = models.ForeignKey(Event)
    price = models.FloatField()
    transaction_type = models.CharField(max_length=30)
    purchase_sale = models.CharField(max_length=30)

class MilkEvent(models.Model):
    def __str__(self):
        return self.event.date
    event  = models.ForeignKey(Event)
    amount = models.FloatField()
	
class MilkRecord(models.Model):
    date = models.DateTimeField()
    period = models.ForeignKey(MilkEvent)
    amount = models.FloatField()

class Picture(models.Model):
    goat = models.ManyToManyField(Goat) # manytomany for multigoat pictures?
    url = models.CharField(max_length=30)
