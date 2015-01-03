from django.contrib import admin
from goats.models import Event, BirthEvent, HealthEvent, TransactionEvent, MilkEvent, MilkRecord, Goat, Herd, UserProfile

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
admin.site.register(UserProfile)
