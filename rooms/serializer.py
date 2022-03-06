

# csv

# DRF
from rest_framework import serializers

# models
from rooms.models import Room


class RoomModelSerializer(serializers.ModelSerializer):
    """Room model serializer"""
    class Meta:
        model = Room
        fields = (
            'id',
            'type_room',
            'price',
        )

