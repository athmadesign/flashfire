from django.shortcuts import render, get_object_or_404
from .models import Banner,Product,ProductImage


def home(request):
    banners = Banner.objects.all()
    trending_products = Product.objects.filter(trending=True)[:6]
    new_arrival_products = Product.objects.filter(new_arrival=True)[:6]

    context = {
        'banners': banners,
        'trending_products': trending_products,
        'new_arrival_products': new_arrival_products,
    }
    return render(request, 'core/index.html', context)



def about_page(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def product(request):
    products = Product.objects.prefetch_related('images').all()  # Efficiently get related images
    return render(request, 'core/product.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})
