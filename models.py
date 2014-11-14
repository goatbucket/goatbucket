from django.db import models

class Herd(models.Model):
    	def __str__(self):
        	return self.name
	name = models.CharField(max_length=30)
	#Goat?

class Goat(models.Model):
    	def __str__(self):
        	return self.name
	name = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30, blank = True)
	status = models.CharField(max_length=30)
	dam = models.ForeignKey("self", related_name="dam", null = True, blank = True)
	sire = models.ForeignKey("self", related_name="sire", null = True, blank = True)
	sex_choices = (('F','Doe'), ('M','Buck'), ('X','Intersex'))
	sex = models.CharField(max_length=1, choices=sex_choices, null = True) 
	herd = models.ForeignKey(Herd, null = True, blank = True)
	birthweight = models.FloatField(null = True, blank = True)
	weight = models.FloatField(null = True, blank = True)#positive numbers only?
	birthday = models.DateTimeField(null = True, blank = True) #want to be able to accept partial data - just the year or m/y
	tag = models.CharField(max_length=30, null = True, blank = True)
	notes = models.CharField(max_length=300, null = True, blank = True)
	#breed
	#coat
	#ears

class GoatRegistration(models.Model):
	goat = models.ForeignKey(Goat)
	registration = models.CharField(max_length=30)
	organization = models.CharField(max_length=30)
	#??????Awards??????

class Event(models.Model):
	date = models.DateTimeField()
	goat_status = models.CharField(max_length=30)
	event_type = models.CharField(max_length=30)
	feed_display = models.BooleanField(default=True)
	goat = models.ManyToManyField(Goat)
	expiration = models.DateTimeField()
	notes = models.CharField(max_length=300)

class BirthEvent(models.Model):
	event  = models.ForeignKey(Event)
	kids = models.ManyToManyField(Goat)

class HealthEvent(models.Model):
	event  = models.ForeignKey(Event)
	healthType = models.CharField(max_length=30)

class TransactionEvent(models.Model):
	event  = models.ForeignKey(Event)
	price = models.FloatField()
	transactionType = models.CharField(max_length=30)
	purchase_sale = models.CharField(max_length=30)

class LactationEvent(models.Model):
	event  = models.ForeignKey(Event)
	amount = models.FloatField()

class Picture(models.Model):
	goat = models.ManyToManyField(Goat) # manytomany for multigoat pictures?
	url = models.CharField(max_length=30)

