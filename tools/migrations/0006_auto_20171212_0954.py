# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20171212_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='story',
            field=models.ManyToManyField(related_name='associated_tools', to='tools.Story'),
        ),
    ]
