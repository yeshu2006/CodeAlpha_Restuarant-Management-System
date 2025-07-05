from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'threshold', 'auto_alert')
    list_filter = ('auto_alert',)
    search_fields = ('name',)
