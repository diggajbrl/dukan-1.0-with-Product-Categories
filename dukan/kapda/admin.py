from django.contrib import admin
from . models import ProductCard

class ProductAdmin (admin.ModelAdmin) :
    list_display =  ('image', 'description', 'size', 'categories', 'currency', 'price')
    list_filter = ('categories',)
    search_fields = ('description',)
admin.site.register(ProductCard, ProductAdmin)