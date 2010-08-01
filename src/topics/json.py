from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse

from voting.models import Vote

from topics.models import Topic

class JSONTopic(object):
    def __init__(self, topic):
        self.topic = topic

    def __freeze__(self, request):
        topic = self.topic
        ctype = ContentType.objects.get_for_model(Topic)
        comment_count = Comment.objects.filter(content_type=ctype.id,
                                               object_pk=topic.id).count()
        score = Vote.objects.get_score(topic)['score']
        has_voted = bool(Vote.objects.get_for_user(topic, request.user))
        has_presenter = bool(list(topic.volunteers.all()))
        return {'topic_id'      : topic.id,
                'title'         : topic.title,
                'description'   : topic.description,
                'creator'       : topic.creator.username,
                'votes'         : score,
                'has_voted'     : has_voted,
                'has_presenter' : has_presenter,
                'url'           : reverse('topic_detail',
                                          kwargs=dict(topic_id=topic.id)),
                'volunteer_url' : reverse('topic_volunteer',
                                          kwargs=dict(topic_id=topic.id)),
                'num_comments'  : comment_count}

class JSONTopicList(object):
    def __init__(self, topics):
        self.topics = topics

    def __freeze__(self, request):
        topic_list = []
        for topic in self.topics:
            topic_list.append(JSONTopic(topic).__freeze__(request))
        topic_list.sort(key = lambda x: (-x['votes'], x['title']))
        return topic_list
