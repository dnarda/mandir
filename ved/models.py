from django.db import models

# Create your models here.

class Event(models.Model):
    description = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200, null = True, blank = True)
    description2 = models.CharField(max_length=200, null = True, blank = True)
    event_start = models.DateTimeField('event start')
    event_end = models.DateTimeField('event end')

class YearlyEvent(models.Model):
    description = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200, null = True, blank = True)
    description2 = models.CharField(max_length=200, null = True, blank = True)
    event_date = models.DateTimeField('event start')

class Darshan(models.Model):
    image_name = models.CharField(max_length=200)
    label = models.CharField(max_length=200, null = True, blank = True)
    data_type = models.CharField(max_length=50, null = True, blank = True)
    display_order = models.IntegerField(null = True)

class Photos(models.Model):
    image_name = models.CharField(max_length=200)
    display_order = models.IntegerField(null = True)
