from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Resource
from .models import Reservation
from .forms import ReservationForm

@login_required
def create_reservation(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, resource=resource, user=request.user)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.resource = resource

            try:
                reservation.save()
                return redirect('my_reservations')
            except Exception as e:
                form.add_error(None, e)

    else:
        form = ReservationForm(resource=resource, user=request.user)

    return render(request, 'reservations/create_reservation.html', {
        'form': form,
        'resource': resource
    })

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)

    return render(request, 'reservations/my_reservations.html', {
        'reservations': reservations
    })