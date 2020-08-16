from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import PlantCreateSerializer


class PlantCreateAPIView(CreateAPIView):
    serializer_class = PlantCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
