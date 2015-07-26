# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 16, 1, 478789, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 16, 15, 958847, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='league',
            field=models.ForeignKey(blank=True, to='athletes.League', null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(blank=True, to='athletes.Team', null=True),
        ),
    ]
