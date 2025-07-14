from django.db import models
import uuid

class Mode(models.Model):
    mode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()

    is_normal = models.BooleanField(null=True, blank=True)
    mode = models.CharField(max_length=255, null=True, blank=True)
    mode_type = models.CharField(max_length=255, null=True, blank=True)
    tenant_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "mode"

    def __str__(self):
        return f"Mode {self.mode_id}"
