from django import forms
from django.forms import fields
from django.forms.widgets import Textarea

from topics.models import Topic

class EditTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['description']

class CreateTopicForm(forms.ModelForm):
    volunteer = fields.BooleanField(required=False, initial=False)

    class Meta:
        model = Topic
        fields = ['title', 'description']

    def save(self, creator=None):
        topic = super(CreateTopicForm, self).save(commit=False)
        if creator:
            topic.creator = creator
        topic.save()
        if self.cleaned_data['volunteer']:
            topic.volunteers.add(creator)
        return topic

class TopicSearchForm(forms.Form):
    title = forms.CharField(required=False)
