from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following")

    def __str__(self):
        return self.username


    Create a custom user model that extends Django’s AbstractUser, adding fields such as bio, profile_picture, and followers (a ManyToMany field referencing itself, symmetrical=False).” task
