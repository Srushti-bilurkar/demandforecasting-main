from django.db import models
import uuid

class GoodsInTransit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    as_on_date = models.DateField(null=True, blank=True)
    client_status = models.CharField(max_length=255, null=True, blank=True)
    eta = models.DateField(null=True, blank=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    shipment_date = models.DateField(null=True, blank=True)
    transit_days = models.IntegerField(null=True, blank=True)

    from_node_id = models.UUIDField(null=True, blank=True)
    sku_id = models.UUIDField(null=True, blank=True)
    to_node_id = models.UUIDField(null=True, blank=True)

    batch_code = models.CharField(max_length=255, null=True, blank=True)
    batch_expiry_date = models.DateField(null=True, blank=True)
    batch_manufacturing_date = models.DateField(null=True, blank=True)

    client_erp_status = models.CharField(max_length=255, null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)

    delivered_order_cost = models.FloatField(default=0.0)
    delivered_order_quantity = models.FloatField(default=0.0)
    in_transit_order_cost = models.FloatField(default=0.0)
    in_transit_order_quantity = models.FloatField(default=0.0)
    item_code = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    pending_order_cost = models.FloatField(default=0.0)
    pending_order_quantity = models.FloatField(default=0.0)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    total_order_cost = models.FloatField(default=0.0)
    total_order_quantity = models.FloatField(default=0.0)

    from_node_code = models.UUIDField(null=True, blank=True)
    from_node_name = models.UUIDField(null=True, blank=True)
    to_node_code = models.UUIDField(null=True, blank=True)
    to_node_name = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "goods_in_transit"

    def __str__(self):
        return f"GoodsInTransit {self.id}"
