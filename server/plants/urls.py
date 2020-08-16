from django.urls import path

from .views import (
    PlantActionTypeListAPIView, PlantCreateAPIView, PlantListAPIView, PlantLocationAPIView,
)

urlpatterns = [
    path('', PlantListAPIView.as_view(), name='plant-list'),
    path('add/', PlantCreateAPIView.as_view(), name='plant-create'),
    path('plant_location/', PlantLocationAPIView.as_view(), name='plant-location'),
    path('action_types/', PlantActionTypeListAPIView.as_view(), name='action-type-list'),
]
