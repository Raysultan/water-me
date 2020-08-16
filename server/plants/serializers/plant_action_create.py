from rest_framework import serializers

from ..models import PlantAction


class PlantActionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAction
        fields = ('action_type', 'plant')
