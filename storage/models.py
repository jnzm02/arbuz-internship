import os
import uuid

from django.db import models
from django.conf import settings


def product_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'product', filename)


class Product(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=product_image_file_path)


class CartCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.cart


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cartCards = models.ManyToManyField('CartCard', related_name='cartCards')
    date = models.CharField(max_length=255)
    time = models.TimeField(max_length=255)
    period = models.IntegerField()

    def __str__(self):
        return self.user.name


class StorageCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)

    def __str__(self):
        return self.storage


class Storage(models.Model):
    storageCards = models.ManyToManyField(CartCard)

    def __str__(self):
        return 'Main Storage'
