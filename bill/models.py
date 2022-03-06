

# Django
from django.db import models

# model
from clients.models import Client


class Bill(models.Model):
    """Bill model"""

    nit = models.CharField(max_length=20, unique=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
