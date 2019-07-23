# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-23 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20190723_1621'),
        ('tools', '0033_create_comment_relations'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='resource_connection',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ToolResourceConnection'),
        ),
        migrations.AddField(
            model_name='toolcategory',
            name='resource_connection',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ToolResourceConnection'),
        ),
    ]
