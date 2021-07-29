from django.contrib import admin
from .models import Product, Cart, ProductImage, Category, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartItem)