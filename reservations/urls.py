from django.urls import path
from .views import create_reservation, my_reservations, admin_reservations, cancel_reservation, update_reservation, cancel_reservation_user

urlpatterns = [
    path('create/<int:resource_id>/', create_reservation, name='create_reservation'),
    path('mine/', my_reservations, name='my_reservations'),
    path('admin/', admin_reservations, name='admin_reservations'),
    path('cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('update/<int:reservation_id>/', update_reservation, name='update_reservation'),
    path('cancel/<int:reservation_id>/', cancel_reservation_user, name='cancel_reservation_user'),
]