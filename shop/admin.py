from django.contrib import admin
from .models import (
    Product
)
# Register your models here.

admin.AdminSite.site_header = 'Shop Scoop'


class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at', 'name')
    list_filter = ('id', 'created_at', 'modified_at', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'id': ('id','name')}