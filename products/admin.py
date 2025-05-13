from django.contrib import admin

from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'is_active')
    list_display_links = ('id', 'name', 'brand')
    list_filter = ('is_active', 'brand', 'category')
    search_fields = ('name', 'brand', 'category')
    list_editable = ('is_active',)