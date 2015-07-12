# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0008_auto_20150424_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birthevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='birthevent',
            name='kids',
        ),
        migrations.RemoveField(
            model_name='event',
            name='goat',
        ),
        migrations.RemoveField(
            model_name='healthevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='milkevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='milkrecord',
            name='period',
        ),
        migrations.RemoveField(
            model_name='transactionevent',
            name='event',
        ),
        migrations.AlterField(
            model_name='goat',
            name='breed',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='goat',
            name='coat',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='goat',
            name='ears',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='goat',
            name='nickname',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='goat',
            name='sex',
            field=models.CharField(default='X', max_length=1, choices=[(b'F', b'Doe'), (b'M', b'Buck'), (b'X', b'Intersex')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goat',
            name='status',
            field=models.CharField(max_length=1, null=True, choices=[(b'A', b'Active'), (b'R', b'Retired'), (b'D', b'Dead'), (b'S', b'Sold')]),
        ),
        migrations.DeleteModel(
            name='BirthEvent',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='HealthEvent',
        ),
        migrations.DeleteModel(
            name='MilkEvent',
        ),
        migrations.DeleteModel(
            name='MilkRecord',
        ),
        migrations.DeleteModel(
            name='TransactionEvent',
        ),
    ]
