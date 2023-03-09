from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='users/', default='users/default_image/default_user_image.png')

    def __str__(self):
        return f"{self.user.username} profile"


