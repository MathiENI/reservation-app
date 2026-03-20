from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ("room", "Salle"),
        ("equipment", "Équipement"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name