from django.contrib.auth.models import User
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

from model_utils.fields import StatusField
from model_utils import Choices

from tools.models import Story, Tool
from comments.models import ThreadedComment


class ActivityEntry(models.Model):
    TYPE_ADD_STORY = 'add_story'
    TYPE_ADD_COMMENT = 'add_comment'
    TYPE_ADD_COMMENT_REPLY = 'add_comment_reply'
    ENTRY_TYPES = Choices(
            TYPE_ADD_STORY,
            TYPE_ADD_COMMENT,
            TYPE_ADD_COMMENT_REPLY
    )
    user = models.ForeignKey('auth.User')
    entry_type = StatusField(choices_name='ENTRY_TYPES')
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    link = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Story)
def on_story_create(sender, instance=None, created=False, **kwargs):
    if created:
        link = reverse('tools:show', args=(instance.tool.id, ))
        ActivityEntry.objects.create(
            user=instance.user,
            entry_type=ActivityEntry.TYPE_ADD_STORY,
            title=instance.tool.title[:150],
            content=instance.content[:500], link=link
        )


@receiver(post_save, sender=ThreadedComment)
def on_comment_create(sender, instance=None, created=False, **kwargs):
    if not created: return

    view = isinstance(instance.related_object, Tool) and 'tools:show'\
            or 'tools:show_story'
    entry_type = instance.parent and ActivityEntry.TYPE_ADD_COMMENT_REPLY\
            or ActivityEntry.TYPE_ADD_COMMENT

    link = reverse(view, args=(instance.related_object.id, ))
    ActivityEntry.objects.create(
        user=instance.author,
        entry_type=entry_type,
        title=instance.related_object.title[:150],
        content=instance.content[:500],
        link=link
    )

# Inject a better __str__ method on the Django User class
User.add_to_class("__str__", User.get_full_name)
