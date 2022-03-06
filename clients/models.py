"""Client model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    """Client model
    """
    email = models.EmailField('email address',unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
