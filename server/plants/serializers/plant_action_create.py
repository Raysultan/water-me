from rest_framework import serializers

from ..models import PlantAction


class PlantActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAction
        fields = ('id', 'created_at', 'action_type', 'plant')
        read_only_fields = ('id', 'created_at')
