from rest_framework import serializers
from .models import (
    Product,
    CartCard,
    Cart,
    StorageCard,
    Storage,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['image']


class CartCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartCard
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cards = CartCardSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = '__all__'


class StorageCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCard
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    cards = StorageCardSerializer(many=True, required=False)

    class Meta:
        model = Storage
        fields = '__all__'
