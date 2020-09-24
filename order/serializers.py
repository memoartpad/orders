from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'client',
            'date_created',
            'date_supply',
            'urgent',
            'warehouse',
            'reference',
            'office_code',
            'partner_code',
            'order_datails',
            'article',
            'quantity',
        ]
