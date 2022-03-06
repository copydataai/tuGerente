"""Reserve models"""

# Typing
from typing import List

# Django
from django.db import models

# models
from clients.models import Client
from bill.models import Bill
from rooms.models import Room

class Reserve(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)
    # DateTime
    start_date: models.DateField = models.DateField('start date of reservation')
    end_date: models.DateField = models.DateField('end date of reservation', blank=True, null=True)

    days_reserved: models.PositiveSmallIntegerField = models.PositiveSmallIntegerField(editable=False)

    # Payments

    # Issue how verify status of the pay
    PAYMENT_STATUS: List = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('DEL', 'Removed')
        ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Pending')

    PAYMENT_CHOICES: List = [
        ('CHECK', 'Check'),
        ('CREDIT','Credit Card'),
        ('DEBIT', 'Debit Card'),
        ('TRANSFER', 'Tranfer')
        ]
    payment_method: models.CharField = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        default='Check'
        )
    payment_amount: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
