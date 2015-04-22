# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0010_auto_20150421_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_start',
        ),
        migrations.RemoveField(
            model_name='priestservice',
            name='location_of_pooja',
        ),
        migrations.RemoveField(
            model_name='priestservice',
            name='type_of_pooja',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default='2015-01-01', verbose_name=b'event start'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priestservice',
            name='pooja_date',
            field=models.CharField(default='2015-01-01', max_length=100, verbose_name=b'Pooja Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priestservice',
            name='pooja_location',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'Location of Pooja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priestservice',
            name='pooja_time',
            field=models.CharField(default='11:00 AM', max_length=100, verbose_name=b'Pooja Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priestservice',
            name='pooja_type',
            field=models.CharField(default=' ', max_length=100, verbose_name=b'Pooja Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yearlyevent',
            name='event_date',
            field=models.DateField(verbose_name=b'event start'),
        ),
    ]
