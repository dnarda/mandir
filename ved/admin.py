from django.contrib import admin

# Register your models here.
from models import Event
from django.contrib import admin

from .models import Event, YearlyEvent, Darshan, Photos, Contact, HallBooking, PriestService

class EventAdmin(admin.ModelAdmin):
        list_display = ('event_date','description')

class YearlyEventAdmin(admin.ModelAdmin):
        list_display = ('event_date','description')

class DarshanAdmin(admin.ModelAdmin):
        list_display = ('image_name','label','data_type')

class PhotosAdmin(admin.ModelAdmin):
        list_display = ('image_name','display_order')

class ContactAdmin(admin.ModelAdmin):
        list_display = ('name','email','subject','message')

class HallBookingAdmin(admin.ModelAdmin):
        list_display = ('name','email','phone','booking_date','booking_time','priest_service_requested')

class PriestServiceAdmin(admin.ModelAdmin):
        list_display = ('name','email','phone','pooja_date','pooja_time','pooja_type','pooja_location')

admin.site.register(Event,EventAdmin)
admin.site.register(YearlyEvent,YearlyEventAdmin)
admin.site.register(Darshan,DarshanAdmin)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(HallBooking,HallBookingAdmin)
admin.site.register(PriestService,PriestServiceAdmin)

