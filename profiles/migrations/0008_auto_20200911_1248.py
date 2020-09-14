# Generated by Django 2.2.8 on 2020-09-11 12:48

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20190925_0951'),
    ]

    operations = [
    migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=True),
        ),
    ]
