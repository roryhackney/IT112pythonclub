from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Minutes, Resource, Event
import datetime

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