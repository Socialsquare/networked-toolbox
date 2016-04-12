
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ThreadedCommentManager(models.Manager):
    def get_query_set(self):
        return super().get_query_set().order_by('tree_id', 'added_dt')

    def get_parents(self):
        return self.get_queryset().filter(parent__isnull=True)


class ThreadedComment(models.Model):
    related_object_type = models.ForeignKey(
        ContentType,
        null=False,
        blank=False
    )
    related_object_id = models.PositiveIntegerField(null=False, blank=False)
    related_object = GenericForeignKey('related_object_type',
                                       'related_object_id')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        default=None,
        related_name='children'
    )
    tree_id = models.IntegerField(null=True, blank=False, db_index=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=False
    )
    content = models.TextField(max_length=settings.COMMENT_MAX_LENGTH)
    added_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    is_removed = models.BooleanField(default=False)
    edited_dt = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['tree_id', 'added_dt']
