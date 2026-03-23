from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reservations.models import Reservation
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard(request):
    now = timezone.now()

    upcoming_reservations = Reservation.objects.filter(
        user=request.user,
        start_datetime__gte=now,
        status="confirmed"
    ).order_by('start_datetime')[:5]

    soon = Reservation.objects.filter(
        user=request.user,
        start_datetime__gte=now,
        start_datetime__lte=now + timedelta(hours=24),
        status="confirmed"
    )

    return render(request, 'dashboard/dashboard.html', {
        'reservations': upcoming_reservations,
        'alerts': soon
    })