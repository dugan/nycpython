import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from nycpython.apps.events.models import Event
from meetup.meetup_api_client import Meetup as MeetupClient

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client = MeetupClient(settings.MEETUP_API_KEY)
        group = client.get_groups(group_urlname=settings.MEETUP_GROUP_NAME).results[0]
        member_count = group.members
        created = datetime.datetime.strptime(group.created, '%a %b %d %H:%M:%S %Z %Y')
        start_date = created.date() - datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=365)

        final_date = datetime.date.today() + datetime.timedelta(days=90)
        while start_date < final_date:
            response = client.get_events(group_id=settings.MEETUP_GROUP_ID, after=end_date.strftime('%m%d%Y'), before=start_date.strftime('%m%d%Y'))
            for event in response.results:
                event_datetime = datetime.datetime.strptime(event.time, '%a %b %d %H:%M:%S %Z %Y')
                e, created = Event.objects.get_or_create(title=event.name, meetup_id=event.id, date=event_datetime.date(),
                                                doors_time=event_datetime.time(), start_time=event_datetime.time(),
                                                num_attendees=event.rsvpcount, description=event.description,
                                                yes_rsvps=event.rsvpcount, no_rsvps=event.no_rsvpcount,
                                                maybe_rsvps=event.maybe_rsvpcount, published=True)
                e.last_meetup_update = datetime.datetime.now()
                #if created:
                #    print 'Created: %s' % event.name
            start_date = end_date
            end_date += datetime.timedelta(days=365)
