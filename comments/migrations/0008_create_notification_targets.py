# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-25 10:50
from __future__ import unicode_literals
from django.apps import apps
from django.db import migrations


class Migration(migrations.Migration):

    def create_notification_targets(apps, schema_editor):

        def create_notifiaction_target(obj):
            Target = apps.get_model('user_notifications', 'NotificationTarget')
            target = Target.objects.create()
            obj.notification_target = target
            obj.save()
            return obj

        Comment = apps.get_model('comments', 'ThreadedComment')
        comments = list(map(create_notifiaction_target, Comment.objects.all()))
    dependencies = [
        ('comments', '0007_threadedcomment_notification_target'),
    ]

    operations = [
        migrations.RunPython(create_notification_targets)
    ]
