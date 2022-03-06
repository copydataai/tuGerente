

# DRF
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# serializers
from bill.serializer import BillModelSerializer

# models
from bill.models import Bill

class BillViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet
        ):
    """Bill view set"""
    serializer_class = BillModelSerializer
    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
