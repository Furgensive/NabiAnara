from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    info_url = models.URLField()

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.FloatField()
    stock = models.IntegerField()
    external_url = models.URLField(blank=True, null=True)  # Новый URL
