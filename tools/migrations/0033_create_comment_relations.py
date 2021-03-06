# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-23 13:40
from __future__ import unicode_literals
from django.apps import apps 
from django.db import migrations, models
import django.db.models.deletion

def create_new_comment_root(apps, schema_editor): 
    from toolz.curried import pipe, map
    from toolz import curry

    @curry
    def create_comment_root_instance(model_class, obj): 
        comment_root = model_class.objects.create()
        obj.comment_root = comment_root
        obj.save()
        return obj
    
    @curry
    def link_comments_to_root(obj): 
        comment_root=obj.comment_root
        ThreadedComment = apps.get_model('comments', 'ThreadedComment')
        comments = ThreadedComment.objects.filter(related_object_id=obj.id)
        comments.update(comment_root=comment_root)
        return obj
        

    CommentRoot = apps.get_model('comments', 'CommentRoot')
    Story = apps.get_model('tools', 'Story')
    Tool = apps.get_model('tools', 'Tool')
    tools = Tool.objects.all()
    stories = Story.objects.all()
    modified_stories = pipe(
        map(create_comment_root_instance(CommentRoot), stories), 
        map(link_comments_to_root), 
        list
    )
    modified_tools = pipe(
        map(create_comment_root_instance(CommentRoot), tools),
        map(link_comments_to_root),
        list
    )

class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_threadedcomment_comment_root'), 
        ('tools', '0032_auto_20190723_1319'),
    ]

    operations = [
        migrations.RunPython(create_new_comment_root), 
        
        
    ]
