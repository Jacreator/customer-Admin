from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    
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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name 


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #one to many relationship
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    status  = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.product.name 
    