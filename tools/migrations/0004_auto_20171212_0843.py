# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20171212_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorygroup',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='story',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='headline',
        ),
        migrations.DeleteModel(
            name='SectionHeadline',
        ),
    ]