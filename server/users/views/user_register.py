from rest_framework import generics, status
from rest_framework.response import Response

from ..models import User
from ..serializers import UserCreateSerializer, UserRetrieveSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request: dict) -> Response:
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=serializer.validated_data['email'])
        return Response(
            data=UserRetrieveSerializer(user).data,
            status=status.HTTP_201_CREATED,
        )
