

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    title= models.CharField(max_length=200)
    price= models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    image= models.CharField(max_length=300)

    def __str__(self):
        return self.title
class Order(models.Model):
 
    
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000, blank=False, null=False)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)