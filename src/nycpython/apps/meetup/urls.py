from django.conf.urls.defaults import *

urlpatterns = patterns('nycpython.apps.meetup.views',
                        url(r'^login/', 'begin_login', name='meetup_login'),
                        url(r'^logout/', 'logout', name='meetup_logout'),
                        url(r'^confirm/', 'confirm', name='meetup_login_confirm'),
                        url(r'^test/', 'test', name='meetup_test'),
                       )

