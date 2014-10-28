from django.db import models

class Goat(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


	Name (CharField)
	Nickname (CharField)
	Status (CharField)
	Dam (Goat)
	Sire (Goat)
	Sex (CharField)
	Herd (ForeignKey)
	BirthWeight (Float)
	Weight (Float)
	Birthday (Datetime)
	Tag (CharField)
	Notes (CharField)
