# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0008_contact_hallbooking_priestservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallbooking',
            name='booking_date',
            field=models.DateField(default='2015-01-01', verbose_name=b'Reservation Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hallbooking',
            name='booking_time',
            field=models.TimeField(default='10:00 AM', verbose_name=b'Reservation Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description1',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description2',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
