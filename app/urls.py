from django.urls import path
from .views import home, contact, products, register, single


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('single/', single, name='single'),
]