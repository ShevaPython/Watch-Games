from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    about_me = models.TextField(blank=True)
    photo = models.ImageField(upload_to='account/photos/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
