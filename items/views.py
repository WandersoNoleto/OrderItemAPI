from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset         = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']
