from django.conf import settings
from django.core.management.base import BaseCommand

from nycpython.meetup.meetup_api_client import Meetup as MeetupClient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client = MeetupClient(settings.MEETUP_API_KEY)
        events = list(Event.live.get_upcoming_events().filter(meetup_id__isnull=False))
        responses = {'yes' : 0, 'no' : 0, 'maybe' : 0 }
        for event in events:
            rsvps = client.get_rsvps(event.meetup_id)
            for rsvp in rsvps:
                responses[rsvp.response] += 1
            event.yes_rsvps = responses['yes']
            event.no_rsvps = responses['no']
            event.maybe_rsvps = responses['maybe']
            event.last_meetup_update = datetime.now()
            event.save()
