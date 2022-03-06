

# DRF
from rest_framework import serializers

# model
from bill.models import Bill


class BillModelSerializer(serializers.ModelSerializer):
    """Bill model serializer"""
    class Meta:
        model = Bill
        fields = ['nit', 'client', 'ammount', 'created']
