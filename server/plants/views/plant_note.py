from rest_framework import generics, response
from rest_framework.permissions import IsAuthenticated

from ..models import PlantNote
from ..serializers import PlantNoteSerializer


class PlantNoteUpdateRetrieveDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantNoteSerializer
    permission_classes = (IsAuthenticated, )
    queryset = PlantNote.objects.all()


class PlantNoteListAPIView(generics.ListAPIView):
    serializer_class = PlantNoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        plant_pk = self.kwargs.get('plant_pk')
        return PlantNote.objects.filter(plant=plant_pk)


class PlantNoteCreateAPIView(generics.CreateAPIView):
    serializer_class = PlantNoteSerializer
    permission_classes = (IsAuthenticated, )
