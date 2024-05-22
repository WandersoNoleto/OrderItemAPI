from django.urls import path
from .views import RegisterView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('auth/', UserLoginView.as_view(), name='user-auth'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
