from django.contrib import admin

from .models import Plant, PlantActionType, PlantLocation, PlantNote, PlantType, PotColor

admin.site.register((
    Plant,
    PlantActionType,
    PlantLocation,
    PlantNote,
    PlantType,
    PotColor,
))
