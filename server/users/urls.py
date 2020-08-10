from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserLoginAPIView, UserRegisterAPIView

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
