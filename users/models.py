from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from carts.models import CartItem


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    mobile = models.IntegerField(max_length=12)
    address = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    zipCode = models.IntegerField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class UserOrder(models.Model):
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order, default=1)
    cart_items = models.ForeignKey(CartItem, default=1)

    def __str__(self):
        return str(self.order) + " " + str(self.user)


class UserContact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name