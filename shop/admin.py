from django.contrib import admin
from .models import (
    Product, Contact, Blog, FAQ
)
# Register your models here.

admin.AdminSite.site_header = 'Shop Scoop'


class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at', 'name')
    list_filter = ('id', 'created_at', 'modified_at', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'name': ('name',)}
    
admin.site.register(Product, AdminProduct)


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'email', 'phone_number')
    list_filter = ('id', 'created_at', 'email', 'phone_number')
    search_fields = ('id', 'email', 'phone_number')
    prepopulated_fields = {'email': ('email',)}

admin.site.register(Contact, AdminContact)


class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title')
    list_filter = ('id', 'created_at', 'title')
    search_fields = ('id', 'title')
    prepopulated_fields = {'title': ('title',)}

admin.site.register(Blog, AdminBlog)


class AdminFAQ(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_filter = ('id', 'created_at', 'question')
    search_fields = ('id', 'question')
    prepopulated_fields = {'question': ('question',)}

admin.site.register(FAQ, AdminFAQ)