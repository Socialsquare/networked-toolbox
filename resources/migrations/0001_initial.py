# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-11 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import resources.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('document', models.FileField(null=True, upload_to=resources.models.do_upload_document)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
