from django.db import models


class Room(models.Model):
    """Room model"""

    TYPE_ROOM = [
        ('SINGLE', 'Single'),
        ('TWIN', 'Twin'),
        ('DOUBLE', 'Double'),
        ('DELUXE', 'Deluxe')
        ]
    type_room = models.CharField(max_length=8, choices=TYPE_ROOM)

    # limit of the price 32767
    price = models.PositiveSmallIntegerField('price per day')

    class Meta:
        """Meta option"""

        ordering = ['type_room', 'price']
