from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['user','created_at','updated_at']

class CartItemSerializer(serializers.ModelSerializer):
    cart=serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'item', 'quantity']