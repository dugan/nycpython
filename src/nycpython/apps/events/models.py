import datetime

from django.db import models

from nycpython.apps.events.managers import EventManager

from nycpython.lib.managers import get_live_manager




class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    published = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    doors_time = models.TimeField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    #host = models.ForeignKey('organizations.Organization', null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    last_meetup_update = models.DateTimeField(null=True, blank=True)
    meetup_id = models.CharField(max_length=50, null=True, blank=True)
    yes_rsvps = models.IntegerField(default=0)
    no_rsvps = models.IntegerField(default=0)
    maybe_rsvps = models.IntegerField(default=0)
    num_attendees = models.IntegerField(default=0)

    objects = EventManager()
    live = get_live_manager(EventManager)()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return "%s on %s" % (self.title, self.date)

    #@models.permalink
    def get_absolute_url(self):
        return "http://www.meetup.com/nycpython/calendar/%s/" % self.meetup_id
        return ('event_detail', (), { 'year' :self.date.year, 'month' :  self.date.month, 'day' : self.date.day })

    def get_previous_published(self):
        try:
            return self.get_previous_by_date(published=True)
        except Event.DoesNotExist:
            return None

    def get_next_published(self):
        try:
            return self.get_next_by_date(published=True)
        except Event.DoesNotExist:
            return None

    @property
    def remaining_slots(self):
        return 40 - self.num_attendees
