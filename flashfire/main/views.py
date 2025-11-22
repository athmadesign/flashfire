from django.shortcuts import render
from .models import Banner

def home(request):
    banners = Banner.objects.all()
    return render(request, 'core/index.html', {'banners': banners})

def about_page(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def product(request):
    return render(request, 'core/product.html')

def product_detail(request):
    return render(request, 'core/product_detail.html')
