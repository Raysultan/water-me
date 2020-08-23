from django.db import models

from .plant import Plant


class PlantNote(models.Model):
    plant = models.ForeignKey(
        to=Plant,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created_at} - {self.title}'
