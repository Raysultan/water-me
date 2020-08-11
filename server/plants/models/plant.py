from django.db import models

from .plant_location import PlantLocation


class Plant(models.Model):
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=250)
    location = models.ForeignKey(
        to=PlantLocation,
        on_delete=models.CASCADE,
    )
    acquire_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.user.get_full_name()} - {self.location}'
