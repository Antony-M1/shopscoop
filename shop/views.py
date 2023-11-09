import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Blog, FAQ
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown

# Create your views here.


def home(request):
    product_details = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_details, 8)

    page = request.GET.get('page')
    try:
        paginated_product_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_product_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_product_details = paginator.page(paginator.num_pages)

    context = {
        'product_data': paginated_product_details,
        'media_url': settings.MEDIA_URL
    }
    return render(request, template_name='shop/home.html', status=200, context=context)


def today_deals(request):
    today = datetime.datetime.now().date()
    product_details = Product.objects.all().order_by('-created_at')
    product_details = product_details.filter(created_at__gte=today)

    paginator = Paginator(product_details, 8)

    page = request.GET.get('page')
    try:
        paginated_product_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_product_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_product_details = paginator.page(paginator.num_pages)

    context = {
        'product_data': paginated_product_details,
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
    blog_details = Blog.objects.all().order_by('-modified_at')
    paginator = Paginator(blog_details, 5)

    page = request.GET.get('page')
    try:
        paginated_blog_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_blog_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_blog_details = paginator.page(paginator.num_pages)

    context = {
        'blog_data': paginated_blog_details,
        'media_url': settings.MEDIA_URL
    }
    return render(request, template_name='shop/blog.html', context=context, status=200)


def faq(request):
    faq_details = FAQ.objects.all()
    paginator = Paginator(faq_details, 10)

    page = request.GET.get('page')
    try:
        paginated_faq_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_faq_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_faq_details = paginator.page(paginator.num_pages)
    
    context = {
        'faq_details': paginated_faq_details
    }

    return render(request, template_name='shop/faq.html', status=200, context=context)


def contact_api(request):
    if request.method == 'POST':
        data = dict(request.POST) if request.POST else None
        if not data:
            response_data = {
                'message': 'Invalid Request'
            }
            return render(request, template_name='shop/contact_response.html', context=response_data)

        data = {
            'email': data.get('email')[0] if isinstance(data.get('email'), list) else data.get('email'),
            'phone_number': data.get('phone_number')[0] if isinstance(data.get('phone_number'), list) else data.get('phone_number'),
            'message': data.get('message')[0] if isinstance(data.get('message'), list) else data.get('message'),
        }
        contact = Contact(**data)
        contact.save()

        response_data = {
            'message1': 'Thanks for contacting us',
            'message2': 'Our team will get back to you in 3 to 5 working days.'
        }
        return render(request, template_name='shop/contact_response.html', context=response_data)



def blog_detail(request, blog_id):
    try:
        blog_data = Blog.objects.get(id=blog_id)
        html_content = markdown.markdown(blog_data.content)
        blog_data.html_content = html_content
        context = {
            'blog': blog_data,
            'html_content': html_content,
            'media_url': settings.MEDIA_URL
        }
        return render(request, template_name='shop/blog_detail.html', context=context)
    except:
        return render(request, 'shop/404.html', status=404)