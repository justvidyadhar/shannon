# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20160218_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
                ('activity_date', models.DateField()),
            ],
        ),
    ]
