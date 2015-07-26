# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0004_auto_20150726_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 55, 33, 750921, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 55, 42, 70845, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='league',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 55, 55, 47034, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='league',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 55, 59, 470900, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 56, 2, 726974, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 56, 9, 942846, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sport',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 56, 13, 886957, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sport',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 17, 56, 17, 286932, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
