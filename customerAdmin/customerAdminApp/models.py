from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    description =  models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    #customer =
    #product =
    date = models.DateField(auto_now_add=True)
    status  = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
