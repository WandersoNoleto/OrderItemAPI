from rest_framework import viewsets, permissions, pagination, status, filters
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from items.models import Item
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend

class OrderPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']


    def create(self, request, *args, **kwargs):
        owner = request.user
        data = request.data
        tag = data.get('tag')
        item_ids = data.get('items', [])

        if not tag or not item_ids:
            return Response({'error': 'Tag and items list are required.'}, status=status.HTTP_400_BAD_REQUEST)

        items = []
        for item_id in item_ids:
            try:
                item = Item.objects.get(id=item_id)
                items.append(item)
            except Item.DoesNotExist:
                return Response({'error': f'Item with ID {item_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(owner=owner, tag=tag)
        order.items.set(items)
        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        tag = data.get('tag', instance.tag)
        item_ids = data.get('items', [])

        if not item_ids:
            return Response({'error': 'Items list is required.'}, status=status.HTTP_400_BAD_REQUEST)

        items = []
        for item_id in item_ids:
            try:
                item = Item.objects.get(id=item_id)
                items.append(item)
            except Item.DoesNotExist:
                return Response({'error': f'Item with ID {item_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        instance.tag = tag
        instance.items.set(items)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
