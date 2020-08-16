from rest_framework import serializers

from ..models import PlantLocation
from ..errors import PlantErrors


class PlantLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantLocation
        fields = ('name',)

    def validate_name(self, name: str) -> str:
        if PlantLocation.objects.filter(name=name.capitalize()).exists():
            raise serializers.ValidationError(PlantErrors.LOCATION_EXISTS)
        return name

    def create(self, validated_data: dict) -> PlantLocation:
        return PlantLocation.objects.create(name=validated_data['name'].capitalize())
