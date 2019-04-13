from django.contrib import admin

from .models import Product

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'preco', )

admin.site.register(Product, ProductsAdmin)