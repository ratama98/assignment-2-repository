from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating  = models.FloatField(
        default=1.00,
        validators = [MaxValueValidator(5.00),MinValueValidator(1.00)]
    )
    release_date = models.DateField()
    review = models.TextField()