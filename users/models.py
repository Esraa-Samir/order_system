from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    currency = models.CharField(max_length=5, help_text="User default currency.", default='EGP')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'is_admin']