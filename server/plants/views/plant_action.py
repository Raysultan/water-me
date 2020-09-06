from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import PlantAction
from ..serializers import PlantActionSerializer


class PlantActionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlantActionSerializer

    def get_queryset(self) -> QuerySet:
        return PlantAction.objects.filter(plant__user=self.request.user)
