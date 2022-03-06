"""Client model"""

# Django
from django.db import models


class Client(models.Model):
    """Client model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True)
    country = models.CharField(
        'country code',
        max_length=5,
        blank=True,
        default='BO'
        )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

