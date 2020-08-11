from django.contrib import admin

from .models import Plant, PlantLocation, PlantNote

admin.site.register((
    Plant,
    PlantLocation,
    PlantNote,
))
