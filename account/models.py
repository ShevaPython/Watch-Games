from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    about_me = models.TextField(blank=True)
    photo = models.ImageField(upload_to='account/photos/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    following = models.ManyToManyField('self',
                                       through='Contact',
                                       related_name='followers',
                                       symmetrical=False)

    def get_absolute_url(self):
        return reverse('account:user_detail', args=[self.username])


class Contact(models.Model):
    user_from = models.ForeignKey(CustomUser,
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser,
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return F"{self.user_from} follows {self.user_to}"
