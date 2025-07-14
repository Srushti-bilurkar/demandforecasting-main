from django.db import models
import uuid

class NodeHierarchy(models.Model):
    node_hierarchy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    node_mapping_id = models.UUIDField()

    class Meta:
        db_table = "node_hierarchy"

    def __str__(self):
        return f"{self.level} - {self.value}"
