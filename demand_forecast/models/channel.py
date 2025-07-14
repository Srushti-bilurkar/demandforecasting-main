import uuid
from django.db import models

class Channel(models.Model):
    channel_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    channel_description = models.TextField(null=True, blank=True)
    channel_name = models.TextField()
    tenant_id = models.UUIDField()

    def __str__(self):
        return self.channel_name
