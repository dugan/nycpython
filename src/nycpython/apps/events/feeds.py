from django.contrib.syndication.feeds import Feed
from nycpython.apps.events.models import Event

class LatestEventFeed(Feed):
    title = "NYC Python: Latest Events"
    link = '/feeds/latest-events/'
    description = 'Events Feed'
    title_template = 'events/feeds/feed_title.html'
    description_template = 'events/feeds/feed_description.html'

    def items(self):
        return Event.objects.all().filter(published=True)[:10]


