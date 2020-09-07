from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(
            validators=[MaxValueValidator(90),MinValueValidator(-90)]
        )
    longitude = models.FloatField(
            validators=[MaxValueValidator(180),MinValueValidator(-180)]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name="locations", on_delete=models.CASCADE
    )
