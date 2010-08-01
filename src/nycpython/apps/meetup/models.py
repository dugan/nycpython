from django.db import models

from nycpython.lib.models import BaseModel

from nycpython.apps.meetup.client import MeetupClient


class MeetupProfile(BaseModel):
    user = models.OneToOneField('auth.User', related_name='meetup')
    meetup_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=200)
    bio = models.TextField(max_length=600)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    access_key = models.CharField(max_length=32)
    secret_key = models.CharField(max_length=32)

    def get_client(self):
        return MeetupClient(self.access_key, self.secret_key)

    def get_absolute_url(self):
        return "http://www.meetup.com/members/%s/" % (self.meetup_id,)
