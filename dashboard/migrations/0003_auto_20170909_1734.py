# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170908_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comic',
            options={'ordering': ['-pull_counter']},
        ),
        migrations.AlterField(
            model_name='comic',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
