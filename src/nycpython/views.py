from nycpython.apps.events.models import Event
from nycpython.lib.decorators import render_to

@render_to('index.html')
def index(request):
    upcoming_event = Event.live.get_upcoming_events()[:1]
    if upcoming_event:
        upcoming_event = upcoming_event[0]
        
    past_events = Event.live.get_past_events()[:5]
    return { 'upcoming_event' : upcoming_event,
             'past_events'    : past_events }
