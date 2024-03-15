from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(choices=STATUS_CHOICES, max_length=6)
