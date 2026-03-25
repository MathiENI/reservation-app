from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random

from catalog.models import Category, Location, Resource
from reservations.models import Reservation


class Command(BaseCommand):
    help = "Seed database with demo data"

    def handle(self, *args, **kwargs):

        self.stdout.write("🌱 Seeding data...")

        # 👤 user
        user, _ = User.objects.get_or_create(username="demo")
        user.set_password("demo")
        user.save()

        # 🏷️ catégories
        categories = []
        for name in ["Salle", "Matériel", "Audio", "Vidéo"]:
            cat, _ = Category.objects.get_or_create(name=name)
            categories.append(cat)

        # 📍 lieux
        locations = []
        for name in ["Paris", "Lyon", "Marseille"]:
            loc, _ = Location.objects.get_or_create(name=name)
            locations.append(loc)

        # 📦 ressources
        resources = []
        for i in range(10):
            res = Resource.objects.create(
                name=f"Ressource {i+1}",
                category=random.choice(categories),
                location=random.choice(locations),
                is_active=True,
                created_by=user,
                updated_by=user
            )
            resources.append(res)

        # 📅 réservations
        for i in range(20):
            start = timezone.now() + timedelta(days=random.randint(0, 5))
            end = start + timedelta(hours=2)

            Reservation.objects.create(
                user=user,
                resource=random.choice(resources),
                start_datetime=start,
                end_datetime=end,
                status=random.choice(["confirmed", "cancelled"]),
                created_by=user,
                updated_by=user
            )

        self.stdout.write(self.style.SUCCESS("✅ Done!"))