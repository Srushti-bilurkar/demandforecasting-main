from django.db import models
import uuid

class SKUHierarchy(models.Model):
    sku_hier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    sku_mapping_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "sku_hierarchy"

    def __str__(self):
        return f"SKUHierarchy {self.level} - {self.value}"
