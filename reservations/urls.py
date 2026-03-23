from django.urls import path
from .views import (
    create_reservation,
    my_reservations,
    admin_reservations,
    cancel_reservation_user,
    cancel_reservation_admin,
    update_reservation,
    export_reservations_csv,
)

urlpatterns = [
    # USER
    path('create/<int:resource_id>/', create_reservation, name='create_reservation'),
    path('mine/', my_reservations, name='my_reservations'),
    path('update/<int:reservation_id>/', update_reservation, name='update_reservation'),
    path('cancel/<int:reservation_id>/', cancel_reservation_user, name='cancel_reservation_user'),

    # ADMIN
    path('admin/reservations/', admin_reservations, name='admin_reservations'),
    path('admin/cancel/<int:reservation_id>/', cancel_reservation_admin, name='cancel_reservation_admin'),
    path('admin/export/', export_reservations_csv, name='export_reservations_csv'),
]