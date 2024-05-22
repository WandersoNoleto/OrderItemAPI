from django.urls import path
from .views import ItemViewSet

urlpatterns = [
    path('', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list-create'),
    path('<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='item-detail')
]