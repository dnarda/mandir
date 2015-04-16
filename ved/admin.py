from django.contrib import admin

# Register your models here.
from models import Event
from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
        list_display = ('event_start','event_end','description')

admin.site.register(Event,EventAdmin)

