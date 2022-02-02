from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    data_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    data_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    status = (
        ('обрабатывается','обрабатывается'),
        ("выехал","выехал"),
        ('доставленно','доставленно')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    data_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=status)

    def __str__(self) -> str:
        return self.product.name
