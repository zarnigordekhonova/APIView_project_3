from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import Category, Products
from .serializers import CategorySerializer, ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.


@api_view(['POST'])
def create_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_products(request, pk=None):
    if pk:
        product = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(product)
    else:
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    serializer = ProductsSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def partial_update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    serializer = ProductsSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
