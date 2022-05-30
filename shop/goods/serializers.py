from dataclasses import field
from rest_framework import serializers
from .models import Product, Storage

class StorageSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')

    class Meta:
        model = Storage
        fields = ('product_name', 'stock')