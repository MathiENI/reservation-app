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
        status="confirmed",
    )

    urgent = now + timedelta(hours=24)

    urgent_reservations = Reservation.objects.filter(
        user=request.user,
        start_datetime__gte=now,
        start_datetime__lte=urgent
    )

    alert_count = urgent_reservations.count()

    cancelled_reservations = Reservation.objects.filter(
        user=request.user,
        status="cancelled",
    )

    reservations = Reservation.objects.filter(user=request.user)

    data = [
        {
            "start_datetime": r.start_datetime.isoformat(),
            "end_datetime": r.end_datetime.isoformat(),
            "resource_name": r.resource.name,
        }
        for r in reservations
    ]

    return render(request, 'dashboard/dashboard.html', {
        'reservations_json': data,
        'reservations': upcoming_reservations,
        "alert_count": alert_count,
        'alerts': soon,
        'cancelled': cancelled_reservations,
    })