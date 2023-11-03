from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500)
    image = models.ImageField(max_length=500, upload_to='images/', null=True, blank=True)
    actual_rate = models.DecimalField(max_digits=10, decimal_places=2)
    offer_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    actual_link = models.TextField(blank=True, null=True)
    affiliate_link = models.TextField(blank=True, null=True)

    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        db_table = "tabProduct"
        verbose_name = 'Product'
        



        
        