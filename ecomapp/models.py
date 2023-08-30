from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    contact=models.CharField(max_length=15)
    img=models.ImageField(blank=True,upload_to="image/",null=True)
    
class Category(models.Model):
    ca=models.CharField(max_length=255)

class Addproduct(models.Model):
    add=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.IntegerField(null=True)
    image=models.ImageField(blank=True,upload_to="image/",null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Addproduct, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
            return self.quantity * self.product.price   