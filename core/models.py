from django.db import models

from accounts.models import User

DELIVERY_STATUS = (
    ("PENDING", "PENDING"),
    ("APPROVED", "APPROVED"),
    ("DELIVERED", "DELIVERED"),

)

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    icon = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    desktop_img = models.ImageField(upload_to="desktop_images")
    mobile_img = models.ImageField(upload_to="desktop_images")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField()
    is_carousel = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="productImages")

    def __str__(self):
        return f"{self.product.name} Image"

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    message = models.TextField()
    by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.product.name} review"


class ShoppingSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    device_id = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        if self.user:
            return f"{self.user.email}  shopping's session"
        else:
            return f"{self.device_id}'s  shopping's session"


class CartItem(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.shopping_session.user} carts Item"

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    building_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.email} address"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    delivery_status = models.CharField(max_length=200,choices=DELIVERY_STATUS, default=DELIVERY_STATUS[0])

    def __str__(self):
        return f"{self.user.email}'s Order"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.user.email} order item"