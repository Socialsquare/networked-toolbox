# Generated by Django 2.2.3 on 2019-08-23 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20190723_1717'),
        ('tools', '0043_create_notification_targets'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolcategory',
            name='resource_connection',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ToolResourceConnection'),
        ),
    ]
