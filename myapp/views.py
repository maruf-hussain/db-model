from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import  *




# Create your views here.
@api_view(['GET'])
def get_products(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return Response(serializer.data)




