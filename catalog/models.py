from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='categories_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='categories_updated')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='locations_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='locations_updated')

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resources_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resources_updated')

    def __str__(self):
        return self.name