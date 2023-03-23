from django.db import models
from core.models import Order
# Create your models here.
class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=200),
    amount = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.phone} -- {self.amount}"