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
