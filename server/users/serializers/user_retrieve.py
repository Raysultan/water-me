from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User


class UserRetrieveSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username',
                  'gender', 'birth_date', 'score', 'token')

    def get_token(self, user: User) -> dict:
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
