from django.contrib import admin
from goats.models import Goat, Herd, GoatEvent
from swingtime import models as swingtime

admin.site.register(Goat)
admin.site.register(Herd)
admin.site.register(GoatEvent)
admin.site.register(swingtime.Occurrence)


