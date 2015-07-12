# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goats', '0011_auto_20150712_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoatEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='swingtime.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('swingtime.event',),
        ),
    ]
