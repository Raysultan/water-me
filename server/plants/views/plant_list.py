from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from ..models import Plant
from ..serializers import PlantListSerializer


class PlantListAPIView(generics.ListAPIView):
    serializer_class = PlantListSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (SearchFilter,)
    search_fields = ('location__id', 'location__name')

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)
