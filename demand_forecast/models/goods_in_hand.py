from django.db import models
import uuid

class GoodsInHand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    as_on_date = models.DateField(null=True, blank=True)
    on_hand_quantity = models.IntegerField(null=True, blank=True)
    reserve_quantity = models.IntegerField(null=True, blank=True)
    sku_per_item_cost = models.FloatField(null=True, blank=True)
    sku_total_cost = models.FloatField(null=True, blank=True)

    node_id = models.UUIDField(null=True, blank=True)
    sku_id = models.UUIDField(null=True, blank=True)

    batch_code = models.CharField(max_length=255, null=True, blank=True)
    batch_expiry_date = models.DateField(null=True, blank=True)
    batch_manufacturing_date = models.DateField(null=True, blank=True)

    blocked_cost = models.CharField(max_length=255, null=True, blank=True)
    blocked_quantity = models.FloatField(default=0.0)

    client_erp_status = models.CharField(max_length=255, null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    in_hand_cost = models.CharField(max_length=255, null=True, blank=True)
    in_hand_quantity = models.IntegerField(default=0)

    item_code = models.CharField(max_length=255, null=True, blank=True)
    item_net_selling_rate = models.FloatField(default=0.0)
    item_per_unit_cost = models.FloatField(default=0.0)
    item_total_cost = models.FloatField(default=0.0)

    item_type = models.CharField(max_length=255, null=True, blank=True)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    reserve_cost = models.CharField(max_length=255, null=True, blank=True)
    returned_cost = models.CharField(max_length=255, null=True, blank=True)
    returned_quantity = models.FloatField(default=0.0)

    class Meta:
        db_table = "goods_in_hand"

    def __str__(self):
        return f"GoodsInHand {self.id}"
