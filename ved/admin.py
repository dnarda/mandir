from django.contrib import admin

# Register your models here.
from models import Event
from django.contrib import admin

from .models import Event, YearlyEvent, Darshan, Photos

class EventAdmin(admin.ModelAdmin):
        list_display = ('event_start','event_end','description')

class YearlyEventAdmin(admin.ModelAdmin):
        list_display = ('event_date','description')

class DarshanAdmin(admin.ModelAdmin):
        list_display = ('image_name','label','data_type')

class PhotosAdmin(admin.ModelAdmin):
        list_display = ('image_name','display_order')

admin.site.register(Event,EventAdmin)
admin.site.register(YearlyEvent,YearlyEventAdmin)
admin.site.register(Darshan,DarshanAdmin)
admin.site.register(Photos,PhotosAdmin)

