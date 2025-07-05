
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    threshold = models.FloatField()
    auto_alert = models.BooleanField(default=False)

    def is_below_threshold(self):
        return self.quantity < self.threshold

    def __str__(self):
        return self.name
