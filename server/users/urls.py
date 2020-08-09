from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegisterAPIView

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
]
