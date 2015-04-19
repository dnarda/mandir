# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ved', '0002_auto_20150417_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Darshan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
