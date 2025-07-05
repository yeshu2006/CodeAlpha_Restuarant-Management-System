from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('reservations/', views.reservation_list, name='reservation_list'),
]
