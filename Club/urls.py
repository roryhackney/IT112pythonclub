from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresources, name='resources'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='detail'),
    path('meetings/', views.getmeetings, name='meetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
]