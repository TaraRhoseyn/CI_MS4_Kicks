# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.db import models
from django.core.validators import MaxValueValidator

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProductGroup(models.Model):
    """
    A class for groups of products, 
    e.g. Womens, Mens and Kids
    """

    name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True)
    friendly_name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True)

    def __str__(self):
        """
        Returns the ProductGroup name string
        Args:
            self (object): self.
        Returns:
            The ProductGroup name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the ProductGroup friendly name string
        Args:
            self (object): self.
        Returns:
            The ProductGroup friendly name string
        """
        return self.friendly_name


class ProductType(models.Model):
    """
    A class for types of products, 
    e.g. trainers, heels etc
    """

    name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True)
    friendly_name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True)

    def __str__(self):
        """
        Returns the ProductType name string
        Args:
            self (object): self.
        Returns:
            The ProductType name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the ProductType friendly name string
        Args:
            self (object): self.
        Returns:
            The ProductType friendly name string
        """
        return self.friendly_name


class ProductBrand(models.Model):
    """
    A class for brands of products, 
    e.g. Nike, Puma etc
    """
    name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )
    friendly_name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )

    def __str__(self):
        """
        Returns the ProductBrand name string
        Args:
            self (object): self.
        Returns:
            The ProductBrand name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the ProductBrand friendly name string
        Args:
            self (object): self.
        Returns:
            The ProductBrand friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class for all products
    """
    sku = models.CharField(
        max_length=12, 
        null=False, 
        blank=False
    )
    name = models.CharField(
        max_length=40, 
        null=False, 
        blank=False
    )
    description = models.TextField()
    product_group = models.ForeignKey(
        'ProductGroup', 
        default=1, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    product_type = models.ForeignKey(
        'ProductType', 
        default=1, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    product_brand = models.ForeignKey(
        'ProductBrand', 
        default=1, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        null=False, 
        blank=False
    )
    rating = models.IntegerField(
        null=False, 
        blank=False, 
        validators=[MaxValueValidator(999)]
    )
    image_url = models.CharField(
        max_length=40, 
        null=False, 
        blank=False, 
        default='SOME STRING'
    )
    has_sizes = models.BooleanField(
        default=True, 
        null=False, 
        blank=False
    )

    def __str__(self):
        """
        Returns the Product name string
        Args:
            self (object): self.
        Returns:
            The Product name string
        """
        return self.name
