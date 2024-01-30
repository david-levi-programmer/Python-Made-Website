from django.db import models
# 'models.Model' defines all common operations
# performed on models in Django


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=80)
    discount = models.FloatField()
