import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    product_details = Product.objects.all()
    context = {
        'product_data': product_details,
        'media_url': settings.MEDIA_URL
    }
    return render(request, template_name='shop/home.html', status=200, context=context)

def today_deals(request):
    today = datetime.datetime.now()
    product_details = Product.objects.all()
    product_details = product_details.filter(created_at__gte=today)
    context = {
        'product_data': product_details,
        'media_url': settings.MEDIA_URL
    }
    return render(request, template_name='shop/today_deals.html', status=200, context=context)

def privacy(request):
    return render(request, template_name='shop/privacy.html', status=200)

def about(request):
    return render(request, template_name='shop/about_us.html', status=200)

def contact(request):
    return render(request, template_name='shop/contact_us.html', status=200)

def chat(request):
    return render(request, template_name='shop/chat.html', status=200)

def blog(request):
    return render(request, template_name='shop/blog.html', status=200)


def contact_api(request):
    if request.method == 'Post':
        data = request.data
        if not data:
            response_data = {
                'message': 'Invalid Request'
            }
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        contact = Contact(**data)
        contact.save()

        response_data = {
            'message': 'Thanks For Contacting Us The ShopScoop Team Will Contact You Back In 48hours'
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
