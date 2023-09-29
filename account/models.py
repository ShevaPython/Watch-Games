from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    about_me = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='account/photos/%Y/%m/%d/', null=True, blank=True)
