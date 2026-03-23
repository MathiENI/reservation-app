# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
from reservations.models import Reservation
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import ResourceForm

@user_passes_test(lambda u: u.is_staff)
def admin_resources(request):
    resources = Resource.objects.all()

    return render(request, 'catalog/admin_resources.html', {
        'resources': resources
    })

@login_required
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
from .models import Resource, Category, Location

def resource_list(request):
    resources = Resource.objects.filter(is_active=True)

    # 🔎 recherche texte
    search = request.GET.get('search')
    if search:
        resources = resources.filter(name__icontains=search)

    # 🎯 filtre type
    resource_type = request.GET.get('type')
    if resource_type:
        resources = resources.filter(type=resource_type)

    # 🏷️ filtre catégorie
    category = request.GET.get('category')
    if category:
        resources = resources.filter(category_id=category)

    # 📍 filtre lieu
    location = request.GET.get('location')
    if location:
        resources = resources.filter(location_id=location)

    # 🔥 filtre disponibilité
    available = request.GET.get('available')
    if available:
        now = timezone.now()

        busy_resources = Reservation.objects.filter(
            start_datetime__lte=now,
            end_datetime__gte=now,
            status="confirmed"
        ).values_list('resource_id', flat=True)

        resources = resources.exclude(id__in=busy_resources)

    return render(request, 'catalog/resource_list.html', {
        'resources': resources,
        'categories': Category.objects.all(),
        'locations': Location.objects.all(),
    })

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    return render(request, 'catalog/resource_detail.html', {
        'resource': resource
    })

@user_passes_test(lambda u: u.is_staff)
def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ressource créée 🎉")
            return redirect('admin_resources')
        else:
            messages.error(request, "Erreur dans le formulaire")

    else:
        form = ResourceForm()

    return render(request, 'catalog/create_resource.html', {
        'form': form
    })

@user_passes_test(lambda u: u.is_staff)
def update_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)

        if form.is_valid():
            form.save()
            messages.success(request, "Ressource modifiée ✏️")
            return redirect('admin_resources')
        else:
            messages.error(request, "Erreur")

    else:
        form = ResourceForm(instance=resource)

    return render(request, 'catalog/update_resource.html', {
        'form': form
    })

@user_passes_test(lambda u: u.is_staff)
def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    resource.is_active = False
    resource.save()

    messages.success(request, "Ressource désactivée ❌")

    return redirect('admin_resources')