# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20150726_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
