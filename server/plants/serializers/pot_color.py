from rest_framework import serializers

from ..models import PotColor


class PotColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = PotColor
        fields = ('id', 'name', 'code')
        read_only_fields = ('id',)
