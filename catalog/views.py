from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
from .models import Resource

def resource_list(request):
    resources = Resource.objects.filter(is_active=True)

    # 🔎 filtre simple
    search = request.GET.get('search')
    if search:
        resources = resources.filter(name__icontains=search)

    return render(request, 'catalog/resource_list.html', {
        'resources': resources
    })

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    return render(request, 'catalog/resource_detail.html', {
        'resource': resource
    })