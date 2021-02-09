from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getresources(request):
    resource_list = Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def resourcedetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'Club/resourcedetail.html', {'resource': resource})

def getmeetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

def meetingdetail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingdetail.html', {'meeting': meeting})