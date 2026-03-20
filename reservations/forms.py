from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.resource = kwargs.pop('resource', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get('start_datetime')
        end = cleaned_data.get('end_datetime')

        if not start or not end:
            return cleaned_data

        if start >= end:
            raise forms.ValidationError("La date de fin doit être après le début.")

        from django.utils import timezone
        if start < timezone.now():
            raise forms.ValidationError("Pas de réservation dans le passé.")

        # 🔥 CONFLIT ICI
        from .models import Reservation

        conflicts = Reservation.objects.filter(
            resource=self.resource,
            start_datetime__lt=end,
            end_datetime__gt=start,
            status="confirmed"
        )

        if conflicts.exists():
            raise forms.ValidationError("Ce créneau est déjà réservé.")

        return cleaned_data

    class Meta:
        model = Reservation
        fields = ['start_datetime', 'end_datetime']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }