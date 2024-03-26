from django.shortcuts import render

# Create your views here.

def home(request):
    ctx = {}
    return render(request, 'blog/index.html', ctx)

def contact(request):
    ctx = {}
    return render(request, 'blog/contact.html', ctx)

def products(request):
    ctx = {}
    return render(request, 'blog/products.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'blog/register.html', ctx)

def single(request):
    ctx = {}
    return render(request, 'blog/single.html', ctx)

