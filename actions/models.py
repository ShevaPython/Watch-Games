from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from account.models import CustomUser


class Action(models.Model):
    """model Actions User"""
    user = models.ForeignKey(CustomUser,
                             related_name='actions',
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['target_ct', 'target_id']),
        ]
