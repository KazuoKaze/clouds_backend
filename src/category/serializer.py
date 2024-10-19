from rest_framework import serializers
from .models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['category', 'slug', 'name',]