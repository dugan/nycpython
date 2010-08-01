from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'nycpython.views.index'), 
    url(r'^events/', include('nycpython.apps.events.urls')),
    url(r'^meetup/', include('nycpython.apps.meetup.urls')),
    url(r'^topics/', include('topics.urls')),
)

if settings.LOCAL_DEVELOPMENT:
    static_url = settings.LOCAL_MEDIA_URL.lstrip('/')
    urlpatterns += patterns("django.views",
        url(r"^%s(?P<path>.*)$" % static_url, "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        }),
    )
    static_url = settings.ADMIN_MEDIA_PREFIX.lstrip('/')
