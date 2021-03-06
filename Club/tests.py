from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Minutes, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Test Meeting', meetingdate=datetime.date(2021, 2, 7), meetingtime='15:00', meetinglocation='Rm 104', meetingagenda='Test Meeting')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='testuser')
        self.type=Meeting.objects.create(meetingtitle='Test Meeting', meetingdate=datetime.date(2021,1,5), meetingtime='14:00', meetinglocation='Rm 104', meetingagenda='test agenda')
        self.min=Minutes.objects.create(meetingname='Test Minutes', meetingid=self.type, minutes='test minutes')
        self.min.attendance.add(self.u)

    def test_string(self):
        self.assertEqual(str(self.min), 'Test Minutes')

    def test_tablename(self):
        self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.user=User(username='testuser', password='123456')
        self.type=Resource(resourcename='Test Resource', resourcetype='Test', resourceurl='https://www.google.com', dateentered=datetime.date(2021, 2, 7), userid=self.user, description='test')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.user=User(username='testuser', password='123456')
        self.type=Event(eventtitle='Test Event', eventlocation='Test Location', eventdate=datetime.date(2021, 2, 8), eventtime='16:00', description='Test event', postedby=self.user)

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Event')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingTest(TestCase):
    #valid form data
    def test_meetingform(self):
        data = {
            'meetingtitle':'Test Meeting',
            'meetingdate':'2021/1/7',
            'meetingtime':'14:00',
            'meetinglocation':'Rm 104',
            'meetingagenda':'Test Agenda'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

#not working
    def test_meetingform_invalid(self):
        data = {
            'meetingtitle':'Test Meeting',
            'meetingdate':'January 3 2021',
            'meetingtime':'14:00',
            'meetinglocation':'Rm 104',
            'meetingagenda':'Test Agenda'
        }
        form=MeetingForm(data)
        self.assertFalse(form.is_valid)

class NewResourceTest(TestCase):
    #valid form data
    def test_resourceform(self):
        data = {
            'resourcename':'Test Resource',
            'resourcetype':'Test Type',
            'resourceurl':'http://www.google.com',
            'datentered':'1/7/2021',
            'userid':'roryhackney',
            'description':'testresource'
        }
        form=ResourceForm(data)
        self.assertTrue(form.is_valid)

#not working
    def test_resourceform_invalid(self):
        data = {
            'resourcetype':'Test Type',
            'resourceurl':'http://www.google.com',
            'datentered':'1/7/2021',
            'userid':'roryhackney',
            'description':'testresource'
        }
        form=ResourceForm(data)
        self.assertFalse(form.is_valid)

class NewResourceAuthenticationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser1', password='P@ssw0rd9')
        self.instance = Resource.objects.create(resourcename='TestResource', resourcetype='TestType', resourceurl='https://www.google.com', dateentered=datetime.date(2021, 3, 5), userid=self.user, description='Test description')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newresource/')

class NewMeetingAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser2', password='P@ssw0rd8')
        self.newmeet = Meeting.objects.create(meetingtitle='Test Meeting', meetingdate=datetime.date(2021, 3, 4), meetingtime='13:00', meetinglocation='Rm 104', meetingagenda='Test Agenda')
    
    def test_redirect_not_logged_in(self):
        resp = self.client.get(reverse('newmeeting'))
        self.assertRedirects(resp, '/accounts/login/?next=/Club/newmeeting/')