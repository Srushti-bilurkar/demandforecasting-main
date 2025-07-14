import uuid
from django.db import models

class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()
    date = models.DateField(null=True, blank=True)
    location_hierarchy_attribute = models.CharField(max_length=255, null=True, blank=True)
    product_hierarchy_attribute = models.CharField(max_length=255, null=True, blank=True)

    # ForeignKey for channel
    channel = models.ForeignKey(
        'Channel',  # Replace 'Channel' with actual model name if different
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='channel'
    )

    def __str__(self):
        return f"Budget {self.id}"

    class Meta:
        db_table = "budget"
