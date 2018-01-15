# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-13 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=8)),
                ('phone_case_pattern', models.ImageField(upload_to=b'')),
                ('phone_type', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=80)),
                ('is_handle', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
