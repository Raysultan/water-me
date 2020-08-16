from rest_framework import serializers

from ..models import Plant
from .plant_action_create import PlantActionCreateSerializer


class PlantCreateSerializer(serializers.ModelSerializer):
    # TODO: make this general purpose and add read_only fields = actions
    class Meta:
        model = Plant
        fields = ('name', 'plant_type', 'pot_color', 'location')
