"""Reserve view set"""

# DRF
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializer
from reserves.serializer import ReserveCreateSerializer, ReserveModelSerializer

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        request.data['client'] = request.user.id
        serializer = ReserveCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reserve = serializer.save()
        data = ReserveModelSerializer(reserve).data
        return Response(data,status=status.HTTP_201_CREATED)
