from django.db import models
import uuid

class NodeType(models.Model):
    node_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    
    node_type_code = models.CharField(max_length=255, null=True, blank=True)
    node_type_title = models.CharField(max_length=255, null=True, blank=True)
    tenant_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "node_type"

    def __str__(self):
        return self.node_type_title or str(self.node_type_id)
