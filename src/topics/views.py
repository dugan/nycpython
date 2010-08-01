# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_POST

import jsonify
from topics.forms import EditTopicForm, CreateTopicForm, TopicSearchForm
from topics.json import JSONTopic, JSONTopicList
from topics.models import Topic
from voting.views import vote_on_object
from voting.models import Vote

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    volunteers = list(topic.volunteers.all())
    if request.user in volunteers:
        volunteers.remove(request.user)
        is_presenter = True
    else:
        is_presenter = False

    ctype = ContentType.objects.get_for_model(topic)
    all_votes = Vote.objects.filter(object_id=topic.id,
                                    content_type=ctype)
    return render_to_response('topics/topic.html',
                                dict(topic=topic,
                                     volunteers=volunteers,
                                     is_presenter=is_presenter,
                                     user=request.user,
                                     all_votes=all_votes),
                              context_instance=RequestContext(request))

def topic_edit(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    form = EditTopicForm(request.POST or None, instance=topic)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('topic_detail',
                                            kwargs=dict(topic_id=topic_id)))
    return render_to_response('topics/topic_edit.html',
                              dict(form=form, topic=topic),
                              context_instance=RequestContext(request))

@require_POST
@login_required
def create_topic_json(request):
    import epdb
    epdb.st()
    form = CreateTopicForm(request.POST)
    if form.is_valid():
        topic = form.save(creator=request.user)
        return HttpResponseRedirect('/')
    return HttpResponse(status=400)

def topic_search_hijax(request):
    key = request.GET['title']
    topics = Topic.objects.filter(Q(title__icontains=key) |
                                  Q(description__icontains=key))
    topics = list(topics)
    for topic in topics:
        # FIXME - Vote has a get_score_in_bulk operation that is broken.
        # should look at why and send a patch
        topic.score = Vote.objects.get_score(topic)['score']
    topics.sort(key=lambda x: (-x.score, x.title))
    if not topics:
        return render_to_response("topics/includes/no_topics.html", 
                                  {'search_term' : key },
                                  context_instance=RequestContext(request))
    return render_to_response("topics/includes/topic_list.html", 
                              {'topics' : topics },
                              context_instance=RequestContext(request))

@login_required
def topic_vote(request, topic_id):
    if request.method != 'POST':
        return HttpResponseNotFound
    return vote_on_object(request, Topic, 'up',
                          object_id=topic_id, allow_xmlhttprequest=True)

@login_required
def topic_volunteer_json(request, topic_id, status=True):
    topic = get_object_or_404(Topic, pk=topic_id)
    if status:
        topic.volunteers.add(request.user)
    else:
        topic.volunteers.remove(request.user)
    return jsonify.response(msg='success')

@login_required
def topic_unvolunteer_json(request, topic_id):
    return topic_volunteer_json(request, topic_id, status=False)

def index(request):
    form = TopicSearchForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data['title']
        topics = Topic.objects.filter(Q(title__icontains=search_term) |
                                      Q(description__icontains=search_term))
    else:
        search_term = ''
        topics = Topic.objects.all()
    topics = list(topics)
    for topic in topics:
        # FIXME - Vote has a get_score_in_bulk operation that is broken.
        # should look at why and send a patch
        topic.score = Vote.objects.get_score(topic)['score']
    topics.sort(key=lambda x: (-x.score, x.title))
    return render_to_response('topics/index.html',
                              dict(topics=topics,
                                   search_term=search_term,
                                   user=request.user),
                              context_instance=RequestContext(request))
