from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import PlantLocation
from ..serializers import PlantLocationSerializer


class PlantLocationAPIView(ListCreateAPIView):
    serializer_class = PlantLocationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = PlantLocation.objects.all()
