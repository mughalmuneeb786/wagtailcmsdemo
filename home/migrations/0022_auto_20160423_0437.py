# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-23 04:37
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20160423_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='form_items', to='home.ContactPage'),
        ),
    ]
