# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0010_auto_20150708_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='alerts',
            field=models.ManyToManyField(to='swingtime.Occurrence', null=True, blank=True),
        ),
    ]
