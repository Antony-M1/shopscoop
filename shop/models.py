from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500)
    actual_rate = models.DecimalField(max_digits=10, decimal_places=2)
    offer_percentage = models.DecimalField(max_digits=3, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        pass
    
    class Meta:
        db_table = "tabProduct"
        verbose_name = 'Product'