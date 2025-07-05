from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order, OrderItem
from tables.models import Table
from menu.models import MenuItem

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            menu_items = form.cleaned_data['menu_items']
            quantities = [int(q) for q in form.cleaned_data['quantities'].split(',')]
            order = Order.objects.create(table=table)
            for idx, item in enumerate(menu_items):
                OrderItem.objects.create(order=order, menu_item=item, quantity=quantities[idx])
            table.is_available = False
            table.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})
