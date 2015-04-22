# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0013_auto_20150422_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description1_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='description2_link',
            field=models.BooleanField(default=False),
        ),
    ]
