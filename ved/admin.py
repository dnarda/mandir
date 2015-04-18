from django.contrib import admin

# Register your models here.
from models import Event
from django.contrib import admin

from .models import Event, YearlyEvent

class EventAdmin(admin.ModelAdmin):
        list_display = ('event_start','event_end','description')

class YearlyEventAdmin(admin.ModelAdmin):
        list_display = ('event_date','description')

admin.site.register(Event,EventAdmin)
admin.site.register(YearlyEvent,YearlyEventAdmin)

