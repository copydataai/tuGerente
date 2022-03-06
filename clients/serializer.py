


from rest_framework import serializers

from clients.models import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'dni', 'country']
