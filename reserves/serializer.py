"""Serializers reserves"""

# Typing

# DRF
from rest_framework import serializers

# models
from reserves.models import Reserve


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
