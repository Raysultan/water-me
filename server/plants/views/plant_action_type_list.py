from rest_framework import generics

from ..models import PlantActionType
from ..serializers import PlantActionTypeRetrieveSerializer


class PlantActionTypeListAPIView(generics.ListAPIView):
    serializer_class = PlantActionTypeRetrieveSerializer
    queryset = PlantActionType.objects.all()
