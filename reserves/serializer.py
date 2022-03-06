"""Serializers reserves"""

# Typing

# DRF
from rest_framework import serializers

# models
from reserves.models import Reserve
from rooms.models import Room
from clients.models import Client
from bill.models import Bill


class ReserveModelSerializer(serializers.ModelSerializer):
    """Reserve model serializer"""
    class Meta:
        model = Reserve
        fields = [
            'room',
            'client',
            'start_date',
            'end_date',
            'days_reserved',
            'payment_status',
            'payment_method',
            'payment_amount',
            ]
        read_only_fields = [
            'days_reserved',
            'payment_amount',
        ]



class ReserveCreateSerializer(serializers.Serializer):
    """Reserve create serializer"""
    room = serializers.IntegerField(required=True)
    client = serializers.IntegerField(required=False)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)

    # Payment
    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('DEL', 'Removed')
        ]
    payment_status = serializers.ChoiceField(choices=PAYMENT_STATUS, required=False)

    PAYMENT_CHOICES = [
        ('CHECK', 'Check'),
        ('CREDIT','Credit Card'),
        ('DEBIT', 'Debit Card'),
        ('TRANSFER', 'Tranfer')
        ]
    payment_method = serializers.ChoiceField(choices=PAYMENT_CHOICES, required=False)


    def create(self, data):
        client = Client.objects.get(id=data['client'])
        room = Room.objects.get(id=data['room'])
        data['room'] = room
        data['client'] = client
        delta = data['end_date'] - data['start_date']
        data['days_reserved'] = delta.days
        data['payment_amount'] = round(delta.days * data['room'].price, 2)
        data['bill'] = Bill.objects.create(client=data['client'], ammount=data['payment_amount'])
        reserve = Reserve.objects.create(**data)
        reserve.save()
        return reserve
