from django.contrib import admin
from .models import Product, Cart, ProductImage, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(Category)