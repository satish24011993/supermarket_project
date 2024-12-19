from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, status

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items':'/list/',
        'Search by Category':'/?category=category_name',
        'Search by Sub Category':'/?subcategory=subcategory_name',
        'Delete Item':'/item/id/delete',
        'Add Item':'/create',
        'Update Item': '/update/id'
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


@api_view(['GET'])
def all_items(request):
    item = None

    if request.query_params:
        item = Item.objects.filter(**request.query_params.dict())
    else:
        item = Item.objects.all()
    if item:
        items_list = ItemSerializer(item, many=True)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(items_list.data)


@api_view(['POST'])
def update(request,id):
    item_data = Item.objects.get(id=id)
    update_item = ItemSerializer(instance = item_data,data=request.data)

    if update_item.is_valid():
        update_item.save()
        return Response(update_item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def delete(request, id):
    item_data = get_object_or_404(Item,id = id)
    item_data.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
    