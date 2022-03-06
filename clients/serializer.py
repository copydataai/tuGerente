

# Django
from django.contrib.auth import password_validation, authenticate

# DRF
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# models
from clients.models import Client

class ClientModelSerializer(serializers.ModelSerializer):
    """Client model serializer"""
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', ]


class ClientSignUpSerializer(serializers.Serializer):
    """Client sign up serializer"""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Client.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        password = data.pop('password_confirmation')
        client = Client.objects.create(**data)
        client.set_password(password)
        client.save()
        return client


class ClientLoginSerializer(serializers.Serializer):
    """Client Login serializer"""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
