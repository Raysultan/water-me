from django.contrib.auth.models import AbstractUser
from django.db import models


class GenderChoices:
    MALE = 'male'
    FEMALE = 'female'

    CHOICES = (
        (FEMALE, 'Женщина'),
        (MALE, 'Мужчина'),
    )


class User(AbstractUser):
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=6,
        choices=GenderChoices.CHOICES,
        blank=True,
        null=True,
    )
    score = models.PositiveSmallIntegerField(
        default=0,
    )

    def __str__(self):
        return self.get_full_name()
