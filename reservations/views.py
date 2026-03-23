from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Resource
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

@user_passes_test(lambda u: u.is_staff)
def admin_reservations(request):
    reservations = Reservation.objects.all().order_by('-start_datetime')
    user_filter = request.GET.get('user')
    if user_filter:
        reservations = reservations.filter(user__username__icontains=user_filter)

    return render(request, 'reservations/admin_reservations.html',  {
        'reservations': reservations
    })

@user_passes_test(lambda u: u.is_staff)
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.status = "cancelled"
    reservation.save()

    return redirect('admin_reservations')

@login_required
def create_reservation(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, resource=resource, user=request.user)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.resource = resource
            reservation.save()
            messages.success(request, "Réservation créée avec succès 🎉")
            return redirect('my_reservations')
        else:
            messages.error(request, "Erreur dans le formulaire")

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

from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # 🔒 sécurité
    if reservation.user != request.user:
        messages.error(request, "Accès interdit.")
        return redirect('my_reservations')

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation, resource=reservation.resource)

        if form.is_valid():
            form.save()
            messages.success(request, "Réservation modifiée avec succès.")
            return redirect('my_reservations')
    else:
        form = ReservationForm(instance=reservation, resource=reservation.resource)

    return render(request, 'reservations/update_reservation.html', {
        'form': form,
        'reservation': reservation
    })

@login_required
def cancel_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if reservation.user != request.user:
        messages.error(request, "Accès interdit.")
        return redirect('my_reservations')

    reservation.status = "cancelled"
    reservation.save()

    messages.success(request, "Réservation annulée.")
    return redirect('my_reservations')