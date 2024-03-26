from django.contrib import admin
from .models import Category, Products, Customer, ShippingAddres, Order, OrderItem, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image', 'created', 'updated')
    list_display_links = ('name',)
    list_filter = ('slug',)
    search_fields = ('name',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price', 'price_type', 'image', 'created', 'updated', 'published')
    list_display_links = ('name',)
    list_filter = ('type',)
    list_editable = ('published',)
    search_fields = ('name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'country', 'city', 'created', 'updated')
    list_display_links = ('full_name',)
    list_filter = ('city',)
    search_fields = ('full_name',)

class ShippingAddresAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'addres', 'city', 'country', 'postal_code', 'created', 'updated')
    list_display_links = ('customer',)
    list_filter = ('city',)
    search_fields = ('customer',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_number', 'total_amount', 'shipping_addres', 'is_completed', 'created')
    search_fields = ('customer',)
    list_filter = ('shipping_addres', 'total_amount')
    list_display_links = ('customer',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'created', 'updated')
    search_fields = ('order',)
    list_display_links = ('order',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'rating', 'created')
    search_fields = ('product', 'customer')
    list_filter = ('rating',)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ShippingAddres, ShippingAddresAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Review, ReviewAdmin)
