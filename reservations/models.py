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
        if not self.start_datetime or not self.end_datetime:
            raise ValidationError("Les dates sont obligatoires.")

        if self.start_datetime >= self.end_datetime:
            raise ValidationError("La date de fin doit être après le début.")

        from django.utils import timezone
        if self.start_datetime < timezone.now():
            raise ValidationError("Pas de réservation dans le passé.")

    def __str__(self):
        return f"{self.resource} - {self.start_datetime}"
