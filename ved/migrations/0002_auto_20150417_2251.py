# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearlyEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('description1', models.CharField(max_length=200, null=True, blank=True)),
                ('description2', models.CharField(max_length=200, null=True, blank=True)),
                ('event_date', models.DateTimeField(verbose_name=b'event start')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='description1',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
