from django.db import models
from django.core.validators import MaxValueValidator


class ProductGroup(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=12, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField()
    product_group = models.ForeignKey(
        'ProductGroup', null=True, blank=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(
        'ProductType', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False)
    rating = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(999)])
    brand = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
