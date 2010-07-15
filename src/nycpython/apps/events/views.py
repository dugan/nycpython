from nycpython.apps.events.models import Event
from nycpython.lib.decorators import render_to

@render_to('events/event_index.html')
def event_index(request):
    event_list = Event.objects.all().filter(published=True).order_by('-date')
    upcoming_events = Event.live.get_upcoming_events()
    past_events = Event.live.get_past_events()

    return {'upcoming_events' : upcoming_events,
            'past_events' : past_events,
            'active_menu': 'Events'}


@render_to('events/event_detail.html')
def event_detail(request, year, month, day ):
    year, month, day = int(year), int(month), int(day)
    event = Event.objects.get(
        published = True,
        date__year = year,
        date__month = month,
        date__day = day,
        )
    #previous_event = event.get_previous_published()
    #next_event = event.get_next_published()
    return {
            'event': event,
            #'previous_event': previous_event,
            #'next_event': next_event,
        }

