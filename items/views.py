from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer
from rest_framework import pagination


class ItemPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ItemViewSet(ModelViewSet):
    queryset         = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPagination
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']
