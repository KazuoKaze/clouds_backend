from django.shortcuts import render

# Create your views here.
from .models import Category, SubCategory
from .serializer import CategorySerializer, SubCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET'])
def get_category(request):
    get_sub_category = SubCategory.objects.all()
    serializer = SubCategorySerializer(get_sub_category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

