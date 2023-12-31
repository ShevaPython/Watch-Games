from django.db import models
from django.utils import timezone
from account.models import CustomUser
from django.urls import reverse
from taggit.managers import TaggableManager

class PostManager(models.Manager):
    """Создания модельного мененджера"""

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Посты"""

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    photo = models.ImageField(upload_to='blog/photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    autor = models.ForeignKey(CustomUser,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    tags = TaggableManager()

    objects = models.Manager()
    published = PostManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return F"{self.title}"

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug])

class CommendManager(models.Manager):
    def queryset(self):

        return super().queryset().filter(status=Commend.Status.PUBLISHED)
class Commend(models.Model):
    """ Creat model commend"""

    class Status(models.IntegerChoices):
        DRAFT = 0, 'NO ACTIVE'
        PUBLISHED = 1, 'ACTIVE'

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    objects = models.Manager()
    published = CommendManager()

    class Meta:
        verbose_name = 'Клментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return F"Comment by {self.name} on {self.post}"