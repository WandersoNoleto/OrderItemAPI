# orders/serializers.py
from rest_framework import serializers
from .models import Order
from items.models import Item
from items.serializers import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'tag', 'items', 'created_at']
        read_only_fields = ['owner']

    def create(self, validated_data):
        return super().create(validated_data)
