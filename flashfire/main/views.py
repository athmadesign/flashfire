from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def base(request):
    return render(request, 'core/base.html')
