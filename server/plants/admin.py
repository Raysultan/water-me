from django.contrib import admin

from .models import (
    Plant, PlantAction, PlantActionType, PlantLocation, PlantNote, PlantType, PotColor
)

admin.site.register((
    Plant,
    PlantAction,
    PlantActionType,
    PlantLocation,
    PlantNote,
    PlantType,
    PotColor,
))
