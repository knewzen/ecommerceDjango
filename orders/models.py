from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from carts.models import Cart, CartItem
from products.models import Product

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # address **
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

    def get_final_amount(self):
        instance = Order.objects.get(id=self.id)
        instance.tax_total = 0.08 * float(self.sub_total)
        instance.final_total = float(self.sub_total) + float(instance.tax_total)
        instance.save()
        return instance.final_total


SHIPPING_CHOICES = (
    ("Received", "Received"),
    ("Shipped", "Shipped"),
    ("Delivered", "Delivered"),
)
class Tracking(models.Model):
    order = models.ForeignKey(Order)
    shipped = models.CharField(max_length=120, choices=SHIPPING_CHOICES, default="Received")
    place1 = models.CharField(max_length=120, null=True, blank=True)
    place3 = models.CharField(max_length=120, null=True, blank=True)
    place4 = models.CharField(max_length=120, null=True, blank=True)
    place5 = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.order.order_id
