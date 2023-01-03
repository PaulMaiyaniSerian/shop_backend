from django.contrib import admin

from .models import (
    Product,
    ProductCategory,
    ProductImage,
    ProductReview,
    ShoppingSession,
    ShippingAddress,
    CartItem,
    Order,
    OrderItem
)
# Register your models here.
models = (
    Product,
    ProductCategory,
    ProductImage,
    ProductReview,
    ShoppingSession,
    ShippingAddress,
    CartItem,
    Order,
    OrderItem
)

admin.site.register(models)