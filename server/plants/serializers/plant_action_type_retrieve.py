from rest_framework import serializers

from ..models import PlantActionType


class PlantActionTypeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantActionType
        fields = ('id', 'name')
