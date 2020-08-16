from django.contrib.auth.password_validation import validate_password
from django.db.models.functions import Lower
from rest_framework import serializers

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
