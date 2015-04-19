# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0003_darshan'),
    ]

    operations = [
        migrations.AddField(
            model_name='darshan',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
    ]
