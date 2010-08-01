from django.contrib import admin
from topics.models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(Topic, TopicAdmin)
