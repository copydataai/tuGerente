"""Client views"""

# DRF
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# serializers
from clients.serializer import (ClientLoginSerializer, ClientSignUpSerializer, ClientModelSerializer)

# model


class ClientLogin(APIView):
    """Client login view"""
    def post(self, request):
        serializer = ClientLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client, token = serializer.save()
        data = {
            'client': ClientModelSerializer(client).data,
            'token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class ClientSignUp(APIView):
    def post(self, request):
        """Client sign up."""
        serializer = ClientSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = ClientModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
