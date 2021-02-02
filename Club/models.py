from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
Models for pythonclub:
Models become tables in the database.
Each model has an autonumbered id by default, can be changed
to declare your own primary keys (not doing that here).
We will use the built-in django User model to store users.

Meeting: meeting title, meeting date, meeting time, location, agenda
Meeting Minutes: meeting id (foreign key), attendance (many to many field with user), minutes (text)
Resource: resource name, resource type, URL, date entered, user id (foreign key with user), description
Event: event title, location, date, time, description, user id of poster
'''
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()
    
    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class Minutes(models.Model):
    meetingname=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.meetingname

    class Meta:
        db_table='minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    description=models.TextField()
    postedby=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'