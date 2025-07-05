from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'menu_items': menu_items})


def home(request):
    return render(request, 'home.html')
