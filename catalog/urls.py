from django.urls import path
from .views import home, resource_list, resource_detail, admin_resources, create_resource, update_resource, \
    delete_resource

urlpatterns = [
    path('', home, name='home'),
    path('resources/', resource_list, name='resource_list'),
    path('resources/<int:resource_id>/', resource_detail, name='resource_detail'),
    path('admin/resources/', admin_resources, name='admin_resources'),
    path('admin/resources/create/', create_resource, name='create_resource'),
    path('admin/resources/update/<int:resource_id>/', update_resource, name='update_resource'),
    path('admin/resources/delete/<int:resource_id>/', delete_resource, name='delete_resource'),
]