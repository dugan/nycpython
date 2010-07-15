from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(blank=True, null=True, editable=False)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, editable=False)
    updated_on = models.DateTimeField(blank=True, null=True, editable=False)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, editable=False)

    class Meta:
        abstract = True
