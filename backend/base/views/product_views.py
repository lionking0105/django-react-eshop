from django.shortcuts import render
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from base.models import Product
from base.products import products
from base.serializers import ProductSerializer

from rest_framework import status


@api_view(['GET', ])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['DELETE', ])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()

    return Response("Product Successfully Deleted")

@api_view(['POST', ])
@permission_classes([IsAdminUser])
def createProduct(request):

    product = Product.objects.create(
        user = request.user,
        name = 'Sample Name',
        price = 0,
        brand = 'Sample Brand',
        countInStock = 0,
        category = 'Sample Category',
        description = 'Sample Description'

    )
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


# @api_view(['CREATE', ])
# @permission_classes([IsAdminUser])
# def updateProduct(request, pk):
#     product = Product.objects.get(_id=pk)
#     serializer = ProductSerializer(product, many=False)

#     return Response(serializer.data)
