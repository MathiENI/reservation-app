from django.urls import path
from .views import home, resource_list, resource_detail, admin_resources

urlpatterns = [
    path('', home, name='home'),
    path('resources/', resource_list, name='resource_list'),
    path('resources/<int:resource_id>/', resource_detail, name='resource_detail'),
    path('admin/resources/', admin_resources, name='admin_resources'),
]