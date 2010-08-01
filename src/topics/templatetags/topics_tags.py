from django.template import Library
from django.template import Context

from topics.forms import TopicSearchForm

register = Library()

@register.inclusion_tag('topics/includes/topic_list.html', takes_context=True)
def render_topic_list(context, topics):
    return Context(context, {'topics' : topics})

@register.inclusion_tag('topics/includes/topic_item.html', takes_context=True)
def render_topic_item(context, topic):
    return Context(context, {'topic' : topic})

@register.inclusion_tag('topics/includes/search_form.html', takes_context=True)
def render_topic_search_form(context, search_term=None):
    initial = {}
    if search_term:
        initial['title'] = search_term
    return {'form' : TopicSearchForm(initial=initial) }

@register.inclusion_tag('topics/includes/user.html', takes_context=True)
def render_topic_user(context, user):
    return { 'user' : user }

@register.inclusion_tag('topics/includes/no_topics.html', takes_context=True)
def render_no_topic_matches(context, search_term):
    return { 'search_term' : search_term }
