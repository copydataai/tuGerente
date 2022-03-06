"""Room views"""

# DRF
from rest_framework import viewsets, mixins

# models
from rooms.models import Room

# serializers
from rooms.serializer import RoomModelSerializer


class RoomViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """Room view set"""
    serializer_class = RoomModelSerializer
    queryset = Room.objects.all()
