# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-23 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20190723_1621'),
        ('tools', '0038_auto_20190723_1646')
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolresource',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='toolresource',
            name='object_id',
        ),
    ]