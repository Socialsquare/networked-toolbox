# Generated by Django 2.2.3 on 2019-07-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20190725_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
