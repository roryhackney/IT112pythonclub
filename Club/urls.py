from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresources, name='resources'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='detail'),
    path('meetings/', views.getmeetings, name='meetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]