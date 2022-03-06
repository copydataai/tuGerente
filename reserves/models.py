"""Reserve models"""

# Typing
from typing import List

# Django
from django.db import models

# models
from clients.models import Client
from rooms.models import Room

class Reserve(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

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


    def save(self, *args, **kwargs):

        if self.end_date:
            # end_date & start_date: datetime.date
            delta = self.end_date - self.start_date
            self.days_reserved = delta.days
            # Define price for room price * days reserved
            self.payment_amount = round(delta.days * self.room.price, 2)
            super(Reserve, self).save(*args, **kwargs)
