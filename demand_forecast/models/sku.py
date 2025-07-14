from django.db import models
import uuid

class SKU(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    
    sku_code = models.CharField(max_length=255)
    sku_name = models.CharField(max_length=255)
    tenant_id = models.UUIDField(null=True, blank=True)
    sku_description = models.CharField(max_length=255, null=True, blank=True)
    
    # Optional: Self-referencing FK (for "like" SKUs)
    like_sku = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='similar_skus'
    )

    class Meta:
        db_table = "sku"

    def __str__(self):
        return f"SKU {self.sku_code} - {self.sku_name}"
