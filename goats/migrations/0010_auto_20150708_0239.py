# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goats', '0009_auto_20150704_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalGoat',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, choices=[(b'F', b'Doe'), (b'M', b'Buck'), (b'X', b'Intersex')])),
                ('birthday', models.DateTimeField(null=True, blank=True)),
                ('birthweight', models.FloatField(null=True, blank=True)),
                ('breed', models.CharField(default=b'', max_length=30, blank=True)),
                ('coat', models.CharField(default=b'', max_length=30, blank=True)),
                ('ears', models.CharField(default=b'', max_length=30, blank=True)),
                ('nickname', models.CharField(default=b'', max_length=30, blank=True)),
                ('status', models.CharField(max_length=1, null=True, choices=[(b'A', b'Active'), (b'R', b'Retired'), (b'D', b'Dead'), (b'S', b'Sold')])),
                ('weight', models.FloatField(null=True, blank=True)),
                ('tag', models.CharField(max_length=30, null=True, blank=True)),
                ('notes', models.CharField(max_length=300, null=True, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical goat',
            },
        ),
        migrations.CreateModel(
            name='HistoricalHerd',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical herd',
            },
        ),
        migrations.AddField(
            model_name='goat',
            name='alerts',
            field=models.ManyToManyField(to='swingtime.Occurrence'),
        ),
        migrations.AddField(
            model_name='historicalgoat',
            name='dam',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='goats.Goat', null=True),
        ),
        migrations.AddField(
            model_name='historicalgoat',
            name='herd',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='goats.Herd', null=True),
        ),
        migrations.AddField(
            model_name='historicalgoat',
            name='history_user',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='historicalgoat',
            name='sire',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='goats.Goat', null=True),
        ),
    ]
