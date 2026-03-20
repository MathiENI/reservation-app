from django.db import models
from django.contrib.auth.models import User
from catalog.models import Resource
from django.core.exceptions import ValidationError
from django.utils import timezone

class Reservation(models.Model):

    STATUS_CHOICES = [
        ("confirmed", "Confirmée"),
        ("cancelled", "Annulée"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="confirmed")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        #Validation des dates
        if self.start_datetime >= self.end_datetime:
            raise ValidationError("La date de fin doit être après la date de début.")

        if self.start_datetime < timezone.now():
            raise ValidationError("Impossible de réserver dans le passé.")

        #Vérification des conflits
        conflicts = Reservation.objects.filter(
            resource=self.resource,
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime,
            status="confirmed"
        ).exclude(id=self.id)

        if conflicts.exists():
            raise ValidationError("Ce créneau est déjà réservé.")

    def __str__(self):
        return f"{self.resource} - {self.start_datetime}"
