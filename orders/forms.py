from django import forms
from menu.models import MenuItem
from tables.models import Table
from .models import Order, OrderItem

class OrderForm(forms.Form):
    table = forms.ModelChoiceField(queryset=Table.objects.none())
    menu_items = forms.ModelMultipleChoiceField(queryset=MenuItem.objects.filter(available=True), widget=forms.CheckboxSelectMultiple)
    quantities = forms.CharField(help_text="Comma-separated quantities for each selected item (e.g. 2,1,3)")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_available=True)

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']
