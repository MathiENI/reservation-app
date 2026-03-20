from django.urls import path
from .views import create_reservation

urlpatterns = [
    path('create/<int:resource_id>/', create_reservation, name='create_reservation'),
]