from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..errors import UserErrors


class UserLoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': UserErrors.CREDENTIALS_ERROR,
    }
