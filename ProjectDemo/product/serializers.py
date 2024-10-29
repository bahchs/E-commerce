from rest_framework import serializers
from .models import Category, Product, Variation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['title', 'slug','description', 'active']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model=Product
        fields=['title','description','category','product_img','price','active']


class VariationSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model=Variation
        fields=['product','title','price','sale_price','inventory']
