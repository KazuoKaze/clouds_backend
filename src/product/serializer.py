from rest_framework import serializers
from .models import Product, ProductVariant, ProductSize, AddImages

class AddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddImages
        fields = ['image',] 


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['name',]  


class ProductVariantSerializer(serializers.ModelSerializer):
    size = ProductSizeSerializer(read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['size', 'price', 'quantity',]  


class ProductSerializer(serializers.ModelSerializer):
    images = AddImageSerializer(many=True, read_only=True)  
    variants = ProductVariantSerializer(many=True, read_only=True)  

    class Meta:
        model = Product
        fields = ['name', 'slug', 'bio', 'images', 'variants',]  



    




    
