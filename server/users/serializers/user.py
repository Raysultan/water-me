from django.contrib.auth.password_validation import validate_password
from django.db.models.functions import Lower
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from ..errors import UserErrors
from ..models import User


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'birth_date',
                  'username', 'confirm_password', 'gender')
        extra_kwargs = {'gender': {'required': False}}

    def validate_email(self, email: str) -> str:
        email = email.lower()
        if User.objects.annotate(lower_email=Lower('email')).filter(lower_email=email).exists():
            raise serializers.ValidationError(UserErrors.EMAIL_EXISTS)
        return email

    def validate_password(self, password: str) -> str:
        validate_password(password)
        return password

    def validate(self, data: dict) -> dict:
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError(UserErrors.PASSWORDS_DIDNT_MATCH)
        return data

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


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
