from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    product_details = Product.objects.all()
    context = {
        'product_data': product_details
    }
    return render(request, template_name='shop/home.html', status=200, context=context)