from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.conf import settings

# Create your views here.

def home(request):
    product_details = Product.objects.all()
    context = {
        'product_data': product_details,
        'media_url': settings.MEDIA_URL
    }
    return render(request, template_name='shop/home.html', status=200, context=context)