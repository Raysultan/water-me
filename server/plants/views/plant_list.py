from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Plant
from ..serializers import PlantListSerializer


class PlantListAPIView(generics.ListAPIView):
    serializer_class = PlantListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)
