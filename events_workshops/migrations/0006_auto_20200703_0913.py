# Generated by Django 2.2.8 on 2020-07-03 09:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_workshops', '0005_auto_20191105_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventworkshop',
            name='participiants',
            field=models.ManyToManyField(related_name='course_participiants', to=settings.AUTH_USER_MODEL),
        ),
    ]