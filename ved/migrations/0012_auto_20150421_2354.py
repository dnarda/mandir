# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0011_auto_20150421_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description1',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
