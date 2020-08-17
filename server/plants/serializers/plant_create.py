from typing import List

from django.db import transaction
from rest_framework import serializers

from ..errors import PlantErrors
from ..models import Plant, PlantAction


class PlantActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAction
        fields = ('action_type', 'created_at')


class PlantCreateSerializer(serializers.ModelSerializer):
    actions = PlantActionSerializer(many=True)

    class Meta:
        model = Plant
        fields = ('name', 'plant_type', 'pot_color', 'location', 'actions')

    def validate_actions(self, actions: List[dict]) -> List[dict]:
        if len(actions) == 0:
            raise serializers.ValidationError(PlantErrors.ACTIONS_EMPTY)
        return actions

    def create(self, validated_data: dict) -> Plant:
        actions = validated_data.pop('actions')
        plant = Plant.objects.create(**validated_data)

        PlantAction.objects.bulk_create([
            PlantAction(**action, plant=plant)
            for action in actions
        ])

        return plant
