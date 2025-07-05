
from django.db import models
from tables.models import Table
from django.utils import timezone

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    reservation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation for {self.name} at {self.reservation_time} (Table {self.table.number})"
