import datetime

from django.db import models

class EventManager(models.Manager):
    def get_upcoming_events(self):
        return self.get_query_set().filter(date__gte=datetime.date.today()).order_by('date')
    
    def get_past_events(self):
        return self.get_query_set().filter(date__lt=datetime.date.today()).order_by('-date')

