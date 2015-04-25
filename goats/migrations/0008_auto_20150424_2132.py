# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0007_auto_20150424_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(max_length=1, null=True, choices=[(b'B', b'Birth'), (b'H', b'Health'), (b'D', b'Death'), (b'T', b'Purchase/Sale'), (b'M', b'New Milk Record'), (b'L', b'New Lactation')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='goat_status',
            field=models.CharField(max_length=1, null=True, choices=[(b'A', b'Active'), (b'D', b'Dead'), (b'S', b'Sold')]),
        ),
    ]
