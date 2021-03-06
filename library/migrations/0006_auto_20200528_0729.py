# Generated by Django 2.2.8 on 2020-05-28 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_create_notification_targets'),
        ('library', '0005_videoresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoresource',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='library.DocumentCategory', verbose_name='Document Category'),
        ),
        migrations.AddField(
            model_name='videoresource',
            name='comment_root',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.CommentRoot'),
        ),
        migrations.AddField(
            model_name='videoresource',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AddField(
            model_name='videoresource',
            name='summary',
            field=models.TextField(help_text='Enter a short summary (max. 1000 characters)', max_length=1000, null=True, verbose_name='Short Summary'),
        ),
        migrations.AddField(
            model_name='videoresource',
            name='title',
            field=models.CharField(help_text='Enter Document Title here.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='videoresource',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date'),
        ),
        migrations.AlterField(
            model_name='librarydocument',
            name='summary',
            field=models.TextField(help_text='Enter a short summary (max. 1000 characters)', max_length=1000, null=True, verbose_name='Short Summary'),
        ),
        migrations.AlterField(
            model_name='librarydocument',
            name='title',
            field=models.CharField(help_text='Enter Document Title here.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='librarydocument',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date'),
        ),
    ]
