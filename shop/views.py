from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, template_name='shop/home.html', status=200)