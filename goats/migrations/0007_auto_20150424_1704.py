# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0006_auto_20150423_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='status',
            field=models.CharField(max_length=1, null=True, choices=[(b'A', b'Active'), (b'D', b'Dead'), (b'S', b'Sold')]),
        ),
    ]
