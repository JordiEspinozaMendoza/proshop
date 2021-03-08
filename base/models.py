from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Name", blank=True)
    image = models.ImageField(null=True, blank=True,
                              default="/placeholder.png")
    brand = models.CharField(max_length=200, null=True,
                             verbose_name="Brand", blank=True)
    category = models.CharField(
        max_length=200, null=True, verbose_name="Category", blank=True)
    description = models.TextField(
        null=True, blank=True, verbose_name="Description")
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Rating", blank=True, null=True)
    numReviews = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Number of Reviews")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Price", blank=True, default=0)
    countInStock = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Count in stock")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Name", blank=True)
    rating = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Rating")
    comment = models.TextField(
        null=True, blank=True, verbose_name="Description")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(
        max_length=200, null=True, verbose_name="Payment Method", blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Tax price", blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Shipping price", blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Total price", blank=True)
    isPaid = models.BooleanField(verbose_name="Is paid?", default=False)
    paidAt = models.DateTimeField(
        auto_now_add=False, verbose_name="Paid at", null=True, blank=True)
    isDelivered = models.BooleanField(
        verbose_name="Is delivered?", default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, verbose_name="Delivered at", null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Name", blank=True)
    qty = models.IntegerField(null=True, blank=True,
                              default=0, verbose_name="Quantity")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Price", blank=True)
    image = models.CharField(max_length=200, null=True,
                             verbose_name="Image", blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(
        max_length=255, null=True, verbose_name="Address", blank=True)
    city = models.CharField(max_length=200, null=True,
                            verbose_name="City", blank=True)
    postalCode = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Postal Code")
    country = models.CharField(
        max_length=200, null=True, verbose_name="Country", blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Price", blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.address
