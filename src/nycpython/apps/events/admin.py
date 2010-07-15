from django.contrib import admin
from nycpython.apps.events.models import Event


class EventAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(Event, EventAdmin)
