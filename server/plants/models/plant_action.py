from django.db import models

from .plant import Plant
from .plant_action_type import PlantActionType


class PlantAction(models.Model):
    created_at = models.DateTimeField()
    action_type = models.ForeignKey(
        to=PlantActionType,
        on_delete=models.CASCADE,
        related_name='actions',
    )
    plant = models.ForeignKey(
        to=Plant,
        on_delete=models.CASCADE,
        related_name='actions',
    )
