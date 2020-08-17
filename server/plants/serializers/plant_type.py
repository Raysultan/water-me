from rest_framework import serializers

from ..models import PlantType


class PlantTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantType
        fields = ('id', 'name')
        read_only_fields = ('id',)
