# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('league', models.ForeignKey(to='athletes.League')),
                ('sport', models.ForeignKey(to='athletes.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='sport',
            field=models.ForeignKey(to='athletes.Sport'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='league',
            field=models.ForeignKey(to='athletes.League'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='sport',
            field=models.ForeignKey(to='athletes.Sport'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(to='athletes.Team'),
        ),
    ]
