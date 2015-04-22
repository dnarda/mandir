# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0012_auto_20150421_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description1',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description2',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
