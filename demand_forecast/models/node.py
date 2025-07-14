from django.db import models
import uuid

class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()

    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)

    # Updated: No GeoDjango needed now
    coordinates = models.TextField(null=True, blank=True)

    description = models.CharField(max_length=255, null=True, blank=True)
    node = models.CharField(max_length=255, null=True, blank=True)
    node_code = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)
    tenant_id = models.UUIDField(null=True, blank=True)
    node_type_id = models.UUIDField(null=True, blank=True)
    activity = models.CharField(max_length=255, null=True, blank=True)
    address_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "node"

    def __str__(self):
        return f"Node {self.node_code or self.id}"
