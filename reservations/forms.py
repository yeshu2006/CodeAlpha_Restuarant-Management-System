from django import forms
from .models import Reservation
from tables.models import Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'name', 'phone', 'reservation_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_available=True)
