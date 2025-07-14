from django.db import models
import uuid

class Network(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()

    bu_id = models.UUIDField(null=True, blank=True)
    from_node_id = models.UUIDField(null=True, blank=True)
    to_node_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "network"

    def __str__(self):
        return f"Network {self.id}"
