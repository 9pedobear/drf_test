from django.db import models

class Car(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True
    )
    price = models.DecimalField(
        max_digits=9, decimal_places=2
    )