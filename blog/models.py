from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slag = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return F"{self.title}"


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'

    PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    tags = models.ManyToManyField('Tag', related_name='posts_tag', blank=True, verbose_name='URL тега')

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return F"{self.title}"
