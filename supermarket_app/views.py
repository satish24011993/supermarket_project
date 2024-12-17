from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, status

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items':'/',
        'Search by Category':'/?category=category_name',
        'Search by Sub Category':'/?subcategory=subcategory_name',
        'Delete Item':'/item/pk/delete',
        'Add Item':'/create',
        'Update Item': '/update/pk'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_item(request):
    # queryset = Item.objects.all()
    item = ItemSerializer(data = request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Item already exist.')
    
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_400_NOT_FOUND)


# @api_view(['GET'])
# def 