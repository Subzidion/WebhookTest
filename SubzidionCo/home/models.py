from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=64, unique=True)
    score = models.DecimalField(max_digits=3, decimal_places=0, 
            validators=[MinValueValidator(0), MaxValueValidator(100)])
    netflix = models.BooleanField(default=False)
    amazonPrime = models.BooleanField(default=False)

    def __str__(self):
        return self.name
