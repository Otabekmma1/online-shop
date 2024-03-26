from django.shortcuts import render

from .models import Category, Products


def home(request):
    ctg = Category.objects.all()
    product = Products.objects.all()
    ctx = {
        'ctg': ctg,
        'product': product
    }
    return render(request, 'blog/index.html', ctx)

def contact(request):
    ctx = {}
    return render(request, 'blog/contact.html', ctx)

def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    product = Products.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'product': product
    }
    return render(request, 'blog/products.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'blog/register.html', ctx)

def single(request):
    ctx = {}
    return render(request, 'blog/single.html', ctx)

