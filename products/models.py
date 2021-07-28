from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


T_SHIRT_SIZE_CHOICES = [('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S')]

SHOES_SIZE_CHOICES = [('45', 45), ('44',44), ('43', 43), ('42', 42), ('41', 41),
                      ('40', 40), ('39', 39), ('38', 38), ('37', 37), ('36', 36),
                      ('35', 35)]

CATEGORY_CHOICES = [('T-SHIRT', 'T-SHIRT'), ('SHOES', 'SHOES')]

SIZE_CHOICES = [
    ('T-SHIRT', T_SHIRT_SIZE_CHOICES),
    ('SHOES', SHOES_SIZE_CHOICES),
]

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length= 150)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField(blank= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.CharField(
        max_length=100,
        choices=SIZE_CHOICES,
    )
    s = models.JSONField(default='{}')

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    default = models.BooleanField(default=False)


class Cart(models.Model):
    quantity = models.PositiveIntegerField()
    SIZE = models.CharField(
        max_length=100,
        choices=SIZE_CHOICES,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
