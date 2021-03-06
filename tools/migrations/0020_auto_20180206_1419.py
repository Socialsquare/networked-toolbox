# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0019_auto_20180206_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='tools.CategoryGroup', verbose_name='Thematic Area'),
        ),
        migrations.AlterField(
            model_name='story',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
    ]
