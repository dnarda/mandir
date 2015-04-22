from django.db import models

# Create your models here.

class Event(models.Model):
    description = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200,  blank = True)
    description1_link = models.BooleanField(default = False)
    description2 = models.CharField(max_length=200,  blank = True)
    description2_link = models.BooleanField(default = False)
    event_date = models.DateField('event start')

class YearlyEvent(models.Model):
    description = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200, null = True, blank = True)
    description2 = models.CharField(max_length=200, null = True, blank = True)
    event_date = models.DateField('event start')

class Darshan(models.Model):
    image_name = models.CharField(max_length=200)
    label = models.CharField(max_length=200, null = True, blank = True)
    data_type = models.CharField(max_length=50, null = True, blank = True)
    display_order = models.IntegerField(null = True)

class Photos(models.Model):
    image_name = models.CharField(max_length=200)
    display_order = models.IntegerField(null = True)

class Contact(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length = 200, verbose_name = "Name")
    email = models.EmailField()
    subject  = models.CharField(max_length = 100)
    message = models.TextField(null = True, blank = True)

class HallBooking(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    phone  = models.CharField(max_length = 30)
    booking_date = models.CharField(max_length = 200,verbose_name = "Reservation Date")
    booking_time = models.CharField(max_length = 200,verbose_name = "Reservation Time")
    priest_service_requested = models.BooleanField(verbose_name = 'Priest Service Required?')
    comments = models.TextField(null = True, blank = True)
    
class PriestService(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    phone  = models.CharField(max_length = 30)
    pooja_date = models.CharField(max_length=100,verbose_name = "Pooja Date")
    pooja_time = models.CharField(max_length=100,verbose_name = "Pooja Time")
    pooja_type = models.CharField(max_length=100,verbose_name = "Pooja Type")
    pooja_location = models.CharField(max_length=100,verbose_name = "Location of Pooja")
    comments = models.TextField(null = True, blank = True)
       
