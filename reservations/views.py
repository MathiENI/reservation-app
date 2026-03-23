from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Resource
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import user_passes_test
import csv
from django.http import HttpResponse

@user_passes_test(lambda u: u.is_staff)
def admin_reservations(request):
    reservations = Reservation.objects.all().order_by('-start_datetime')

    # 👤 filtre utilisateur
    user = request.GET.get('user')
    if user:
        reservations = reservations.filter(user__username__icontains=user)

    # 📦 filtre ressource
    resource = request.GET.get('resource')
    if resource:
        reservations = reservations.filter(resource__name__icontains=resource)

    # 📅 filtre date début
    start = request.GET.get('start')
    if start:
        reservations = reservations.filter(start_datetime__gte=start)

    # 📅 filtre date fin
    end = request.GET.get('end')
    if end:
        reservations = reservations.filter(end_datetime__lte=end)

    return render(request, 'reservations/admin_reservations.html', {
        'reservations': reservations
    })

@user_passes_test(lambda u: u.is_staff)
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.status = "cancelled"
    reservation.save()

    return redirect('admin_reservations')

@user_passes_test(lambda u: u.is_staff)
def cancel_reservation_admin(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reason = request.POST.get('reason')

        reservation.status = "cancelled"
        reservation.reason = reason
        reservation.save()

        messages.success(request, "Réservation annulée avec motif 🧾")
        return redirect('admin_reservations')

    return render(request, 'reservations/cancel_with_reason.html', {
        'reservation': reservation
    })

@login_required
def create_reservation(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, resource=resource, user=request.user)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.resource = resource
            # 🔥 JOURNALISATION
            reservation.created_by = request.user
            reservation.updated_by = request.user

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
            # 🔥 JOURNALISATION
            reservation.updated_by = request.user

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

@user_passes_test(lambda u: u.is_staff)
def export_reservations_csv(request):
    reservations = Reservation.objects.all()

    # 📅 filtres période
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start:
        reservations = reservations.filter(start_datetime__gte=start)

    if end:
        reservations = reservations.filter(end_datetime__lte=end)

    # 📄 réponse CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reservations.csv"'

    writer = csv.writer(response)

    # 🧾 header
    writer.writerow([
        'Utilisateur',
        'Ressource',
        'Début',
        'Fin',
        'Statut',
        'Créé le',
    ])

    # 📊 données
    for r in reservations:
        writer.writerow([
            r.user.username,
            r.resource.name,
            r.start_datetime,
            r.end_datetime,
            r.status,
            r.created_at,
        ])

    return response