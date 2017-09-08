# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170909_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comic',
            options={'ordering': ['weekly_index']},
        ),
        migrations.RemoveField(
            model_name='comic',
            name='pull_counter',
        ),
        migrations.AddField(
            model_name='comic',
            name='weekly_index',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
