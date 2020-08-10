from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers import UserLoginSerializer


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
