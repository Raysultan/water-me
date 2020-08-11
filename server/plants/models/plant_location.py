from django.db import models


# model for internal user
# creation and adjustments made only from admin panel
class PlantLocation(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
    )

    def __str__(self):
        return self.name
