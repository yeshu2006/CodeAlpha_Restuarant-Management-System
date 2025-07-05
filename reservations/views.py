from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from tables.models import Table

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            table = reservation.table
            table.is_available = False
            table.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reserve_table.html', {'form': form})

def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-reservation_time')
    return render(request, 'reservation_list.html', {'reservations': reservations})
