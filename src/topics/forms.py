from django import forms
from django.forms import fields

from topics.models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['description']

class JSONTopicForm(forms.ModelForm):
    volunteer = fields.BooleanField(required=False, initial=False)

    class Meta:
        model = Topic
        fields = ['title', 'description']

    def save(self, creator=None):
        topic = super(JSONTopicForm, self).save(commit=False)
        if creator:
            topic.creator = creator
        topic.save()
        if self.cleaned_data['volunteer']:
            topic.volunteers.add(creator)
        return topic
