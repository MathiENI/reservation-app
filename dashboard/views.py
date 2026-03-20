from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reservations.models import Reservation
from django.utils import timezone

@login_required
def dashboard(request):
    now = timezone.now()

    upcoming_reservations = Reservation.objects.filter(
        user=request.user,
        start_datetime__gte=now,
        status="confirmed"
    ).order_by('start_datetime')[:5]

    return render(request, 'dashboard/dashboard.html', {
        'reservations': upcoming_reservations
    })