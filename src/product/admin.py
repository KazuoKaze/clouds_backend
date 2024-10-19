from django.contrib import admin
from .models import Product, ProductSize, ProductVariant, AddImages

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1  

class AddImagesInline(admin.TabularInline):
    model = AddImages
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    inlines = [AddImagesInline, ProductVariantInline]
    list_display = ('name', 'timestamp')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSize)