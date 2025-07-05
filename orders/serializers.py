from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'created_at', 'orderitem_set', 'total_amount']

    def get_total_amount(self, obj):
        return obj.total_amount()
