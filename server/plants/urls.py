from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PlantActionTypeListAPIView, PlantActionViewSet, PlantCreateAPIView, PlantListAPIView,
    PlantLocationAPIView, PlantNoteCreateAPIView, PlantNoteListAPIView,
    PlantNoteUpdateRetrieveDeleteAPIView, PlantUpdateRetrieveDeleteAPIView
)

router = DefaultRouter()
router.register('', PlantActionViewSet, basename='actions')

urlpatterns = [
    path('actions/', include(router.urls)),

    path('', PlantListAPIView.as_view(), name='plant-list'),
    path('add/', PlantCreateAPIView.as_view(), name='plant-create'),
    path('<str:pk>/', PlantUpdateRetrieveDeleteAPIView.as_view(), name='plant-create'),
    path('plant_location/', PlantLocationAPIView.as_view(), name='plant-location'),
    path('action_types/', PlantActionTypeListAPIView.as_view(), name='action-type-list'),
    path('notes/list/<str:plant_pk>/', PlantNoteListAPIView.as_view(), name='plant-note-list'),
    path('notes/add/', PlantNoteCreateAPIView.as_view(), name='plant-note-list'),
    path('notes/<str:pk>/', PlantNoteUpdateRetrieveDeleteAPIView.as_view(), name='plant-note'),
]
