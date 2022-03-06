"""Client views"""

# DRF
from rest_framework import viewsets, mixins

# serializers
from clients.serializer import ClientModelSerializer

# model
from clients.models import Client

class ClientViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """Client view set"""
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
