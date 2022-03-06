

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