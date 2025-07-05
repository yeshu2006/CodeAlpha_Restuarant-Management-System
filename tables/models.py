
from django.db import models

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_available = models.BooleanField(default=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"
