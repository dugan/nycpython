import datetime

from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField()
    creator = models.ForeignKey('auth.User', related_name='created_topics')
    volunteers = models.ManyToManyField('auth.User',
                                        related_name='volunteered_topics')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('topic_detail', None, {'topic_id' : self.id})

    def save(self):
        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()
        super(Topic, self).save()

    class Meta:
        ordering = ('title',)
