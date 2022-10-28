from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/')
    phone = models.CharField(max_length=20, null=True, blank=True)
    instagram_username = models.CharField(max_length=20, null=True, blank=True)
    telegram_username = models.CharField(max_length=20, null=True, blank=True)