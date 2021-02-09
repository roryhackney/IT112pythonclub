from django.shortcuts import render
from .models import Meeting, Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getresources(request):
    resource_list = Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})