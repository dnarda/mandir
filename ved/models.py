from django.db import models

# Create your models here.

class Event(models.Model):
	description = models.CharField(max_length=200)
	event_start = models.DateTimeField('event start')
	event_end = models.DateTimeField('event end')
