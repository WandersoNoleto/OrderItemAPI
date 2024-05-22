from django.urls import path
from .views import RegisterView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
