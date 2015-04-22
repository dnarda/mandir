# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0009_auto_20150421_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallbooking',
            name='booking_date',
            field=models.CharField(max_length=200, verbose_name=b'Reservation Date'),
        ),
        migrations.AlterField(
            model_name='hallbooking',
            name='booking_time',
            field=models.CharField(max_length=200, verbose_name=b'Reservation Time'),
        ),
        migrations.AlterField(
            model_name='hallbooking',
            name='priest_service_requested',
            field=models.BooleanField(verbose_name=b'Priest Service Required?'),
        ),
    ]
