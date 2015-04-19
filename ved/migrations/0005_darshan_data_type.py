# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0004_darshan_display_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='darshan',
            name='data_type',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
