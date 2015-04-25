from django.contrib import admin
<<<<<<< HEAD
from goats.models import Event, BirthEvent, HealthEvent, TransactionEvent, MilkEvent, MilkRecord, Goat, Herd
=======
from goats.models import Event, BirthEvent, HealthEvent, TransactionEvent, MilkEvent, MilkRecord, Goat, Herd, UserProfile
>>>>>>> f6121c5250e855357ba8fe21066572889d22ddbd

class MilkLine(admin.TabularInline):
    model = MilkRecord
    extra = 7
class MilkEventAdmin(admin.ModelAdmin):
    inlines = [MilkLine]
admin.site.register(Event)
admin.site.register(BirthEvent)
admin.site.register(HealthEvent)
admin.site.register(TransactionEvent)
admin.site.register(MilkEvent, MilkEventAdmin)
admin.site.register(Goat)
admin.site.register(Herd)
<<<<<<< HEAD
=======
admin.site.register(UserProfile)
>>>>>>> f6121c5250e855357ba8fe21066572889d22ddbd
