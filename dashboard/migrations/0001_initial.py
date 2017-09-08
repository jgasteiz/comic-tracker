# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('external_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('publisher', models.CharField(blank=True, max_length=128)),
                ('release_date', models.CharField(blank=True, max_length=128)),
                ('price', models.CharField(blank=True, max_length=128)),
                ('description', models.TextField(blank=True)),
                ('cover_url', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
