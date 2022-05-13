from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class House:
    rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    garages = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    toilets = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    addresse_house = models.CharField(max_length=30, blank=False)
    lat = models.CharField(max_length=50)
    long_ = models.CharField(max_length=50)
    