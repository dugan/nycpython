from django.conf.urls.defaults import *
from nycpython.apps.events.models import Event
from nycpython.apps.events.feeds import LatestEventFeed

urlpatterns = patterns('nycpython.apps.events.views',
                       url(r'^$', 'event_index', name='event_index'),
                       url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'event_detail', name='event_detail',),
                       )

feeds = {
    'latest-events': LatestEventFeed,
         }

urlpatterns += patterns('',
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
                        )
