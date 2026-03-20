# Register your models here.
from django.contrib import admin
from .models import Category, Location, Resource

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Resource)