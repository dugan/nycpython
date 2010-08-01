from django.conf.urls.defaults import patterns, url, include

topic_detail_patterns = patterns('topics.views',
    url(r'^edit$',        'topic_edit',             name='topic_edit'),
    url(r'^vote$',        'topic_vote',             name='topic_vote'),
    url(r'^volunteer$',   'topic_volunteer_json',   name='topic_volunteer'),
    url(r'^unvolunteer$', 'topic_unvolunteer_json', name='topic_unvolunteer'),
    url(r'^$',            'topic_detail',           name='topic_detail'))

urlpatterns = patterns('topics.views',
    url(r'^(?P<topic_id>\d+)/',   include(topic_detail_patterns)),
    url(r'^search/$',             'topic_search_json', name='topic_search'),
    url(r'^create/$',             'create_topic_json', name='create_topic'),
    url(r'^$',                    'index', name='topic_index'),
)

