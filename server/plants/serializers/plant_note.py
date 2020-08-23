from rest_framework import serializers

from ..models import PlantNote


class PlantNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantNote
        fields = ('id', 'created_at', 'plant', 'title', 'text')
        read_only_fields = ('id', 'created_at',)
