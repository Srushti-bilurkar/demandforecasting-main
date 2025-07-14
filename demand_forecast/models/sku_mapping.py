import uuid
from django.db import models

class SKUMapping(models.Model):
    sku_mapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    bu_id = models.UUIDField()

    currency = models.CharField(max_length=255)
    ebitdta_unit_pct = models.FloatField()
    gross_margin_unit_pct = models.FloatField()

    lifecycle_end_date = models.DateField(null=True, blank=True)
    lifecycle_start_date = models.DateField(null=True, blank=True)
    lifecycle_sunset_date = models.DateField(null=True, blank=True)
    product_lifecycle_status = models.BooleanField()

    unit_of_measure = models.CharField(max_length=255)
    unit_price = models.FloatField()
    volume = models.BigIntegerField()
    volume_unit_of_measure = models.CharField(max_length=255)
    weight = models.FloatField()
    weight_unit_of_measure = models.CharField(max_length=255)

    # Foreign Keys
    channel = models.ForeignKey("Channel", on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.ForeignKey("SKU", on_delete=models.SET_NULL, null=True, blank=True)

    breadth = models.IntegerField(default=0)
    length = models.IntegerField(null=True, blank=True)
    max_order_quantity = models.FloatField(null=True, blank=True)
    max_shelf_life = models.IntegerField(null=True, blank=True)
    min_order_quantity = models.FloatField(null=True, blank=True)
    net_weight = models.FloatField(null=True, blank=True)
    net_weight_uom = models.CharField(max_length=255, null=True, blank=True)
    sku_sales_type = models.CharField(max_length=255, null=True, blank=True)
    sku_stock_type = models.CharField(max_length=255, null=True, blank=True)
    unit_price_cogs = models.FloatField(null=True, blank=True)
    unit_price_nsr = models.FloatField(null=True, blank=True)
    unit_price_sp = models.FloatField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)

    additional_info = models.JSONField(null=True, blank=True)
    bom_code = models.CharField(max_length=255, null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    case_size = models.FloatField(default=0.0)
    lot_size = models.FloatField(default=0.0)
    manufacturing_cost = models.FloatField(default=0.0)
    manufacturing_lead_time = models.IntegerField(default=0)
    min_shelf_life = models.BigIntegerField(default=0)

    class Meta:
        db_table = "sku_mapping"

    def __str__(self):
        return f"SKUMapping {self.sku_mapping_id}"
