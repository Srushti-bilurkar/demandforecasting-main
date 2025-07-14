from django.db import models
import uuid

class Personnel(models.Model):
    personnel_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    location_hierarchy_attribute = models.CharField(max_length=255, null=True, blank=True)
    sku_hierarchy_attribute = models.CharField(max_length=255, null=True, blank=True)

    # Foreign keys (replace UUID fields)
    channel = models.ForeignKey(
        'Channel',  # Replace with actual model name for channel if different
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='channel'
    )
    node = models.ForeignKey(
        'NodeMapping',  # Assuming it links to NodeMapping table
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='node_id'
    )
    sku = models.ForeignKey(
        'SKU',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sku_id'
    )

    class Meta:
        db_table = "personnel"

    def __str__(self):
        return f"Personnel {self.personnel_id}"
