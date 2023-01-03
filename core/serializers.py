from rest_framework import serializers
from .models import (
    Product, 
    ProductCategory, 
    ShoppingSession,
    CartItem,
    )

class ProductSerializer(serializers.ModelSerializer):

    desktop_img = serializers.ImageField(use_url=True,required=False)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ShoppingSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingSession
        fields = "__all__"



class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"