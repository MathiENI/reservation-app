from django.urls import path
from .views import (
    admin_resources,
    create_resource,
    update_resource,
    delete_resource,

    admin_categories,
    create_category,
    update_category,
    delete_category,

    admin_locations,
    create_location,
    update_location,
    delete_location,
)

urlpatterns = [
    # 🧱 Ressources
    path('resources/', admin_resources, name='admin_resources'),
    path('resources/create/', create_resource, name='create_resource'),
    path('resources/update/<int:resource_id>/', update_resource, name='update_resource'),
    path('resources/delete/<int:resource_id>/', delete_resource, name='delete_resource'),

    # 🏷️ Catégories
    path('categories/', admin_categories, name='admin_categories'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/update/<int:category_id>/', update_category, name='update_category'),
    path('categories/delete/<int:category_id>/', delete_category, name='delete_category'),

    # 📍 Lieux
    path('locations/', admin_locations, name='admin_locations'),
    path('locations/create/', create_location, name='create_location'),
    path('locations/update/<int:location_id>/', update_location, name='update_location'),
    path('locations/delete/<int:location_id>/', delete_location, name='delete_location'),
]