"""Reserve view set"""

# DRF
from rest_framework import mixins, viewsets

# Serializer
from reserves.serializer import ReserveModelSerializer

# Models
from reserves.models import Reserve


class ReserverViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet
        ):
    """Reserve view set"""

    serializer_class = ReserveModelSerializer
    queryset = Reserve.objects.all()
