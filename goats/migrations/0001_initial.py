# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('expiration', models.DateTimeField()),
                ('goat_status', models.CharField(max_length=30)),
                ('event_type', models.CharField(max_length=30)),
                ('feed_display', models.BooleanField(default=True)),
                ('notes', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30, blank=True)),
                ('status', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, null=True, choices=[(b'F', b'Doe'), (b'M', b'Buck'), (b'X', b'Intersex')])),
                ('birthweight', models.FloatField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
                ('birthday', models.DateTimeField(null=True, blank=True)),
                ('tag', models.CharField(max_length=30, null=True, blank=True)),
                ('notes', models.CharField(max_length=300, null=True, blank=True)),
                ('breed', models.CharField(max_length=30, null=True, blank=True)),
                ('coat', models.CharField(max_length=30, null=True, blank=True)),
                ('ears', models.CharField(max_length=30, null=True, blank=True)),
                ('dam', models.ForeignKey(related_name='mammy', blank=True, to='goats.Goat', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoatRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=30)),
                ('goat', models.ForeignKey(to='goats.Goat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HealthEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health_type', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='goats.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Herd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MilkEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('event', models.ForeignKey(to='goats.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MilkRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('period', models.ForeignKey(to='goats.MilkEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=30)),
                ('goat', models.ManyToManyField(to='goats.Goat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransactionEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('transaction_type', models.CharField(max_length=30)),
                ('purchase_sale', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='goats.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='herd',
            name='user',
            field=models.ForeignKey(to='goats.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goat',
            name='herd',
            field=models.ForeignKey(blank=True, to='goats.Herd', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goat',
            name='sire',
            field=models.ForeignKey(related_name='pappy', blank=True, to='goats.Goat', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='goat',
            field=models.ManyToManyField(to='goats.Goat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='birthevent',
            name='event',
            field=models.ForeignKey(to='goats.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='birthevent',
            name='kids',
            field=models.ManyToManyField(to='goats.Goat'),
            preserve_default=True,
        ),
    ]
