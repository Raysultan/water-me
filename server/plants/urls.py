from django.urls import path

from .views import PlantActionTypeListAPIView, PlantListAPIView

urlpatterns = [
    path('', PlantListAPIView.as_view(), name='plant-list'),
    path('action_types/', PlantActionTypeListAPIView.as_view(), name='action-type-list'),
]
