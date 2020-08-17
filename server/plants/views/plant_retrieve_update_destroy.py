from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Plant
from ..serializers import PlantUpdateRetrieveDeleteSerializer


class PlantUpdateRetrieveDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantUpdateRetrieveDeleteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)
