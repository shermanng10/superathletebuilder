# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20150726_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='updated_at',
        ),
    ]
