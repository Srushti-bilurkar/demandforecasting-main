from django.db import models
import uuid
from .sku import SKU
from .channel import Channel
from .node_mapping import NodeMapping  # assuming node_id refers to Node model

class SKUNodeMapping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    
    bu_id = models.UUIDField(null=True, blank=True)
    bu_description = models.CharField(max_length=255, null=True, blank=True)

    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True, blank=True)
    node = models.ForeignKey(NodeMapping, on_delete=models.SET_NULL, null=True, blank=True)

    cost_manufacturing_uom = models.CharField(max_length=255, null=True, blank=True)
    cost_manufacturing_unit = models.FloatField(null=True, blank=True)
    cost_warehouse_uom = models.CharField(max_length=255, null=True, blank=True)
    cost_warehouse_unit = models.FloatField(null=True, blank=True)

    cycle_time_manufacturing_uom = models.CharField(max_length=255, null=True, blank=True)
    cycle_time_manufacturing_unit = models.FloatField(null=True, blank=True)
    cycle_time_warehouse_uom = models.CharField(max_length=255, null=True, blank=True)
    cycle_time_warehouse_unit = models.FloatField(null=True, blank=True)

    is_demand_node = models.BooleanField(null=True, blank=True)
    is_distribution_node = models.BooleanField(null=True, blank=True)
    is_manufacturing_node = models.BooleanField(null=True, blank=True)

    mapping_start_date = models.DateField(null=True, blank=True)
    mapping_end_date = models.DateField(null=True, blank=True)
    mapping_sunset_date = models.DateField(null=True, blank=True)
    mapping_life_cycle_status = models.BooleanField(null=True, blank=True)

    manufacturing_capacity_uom = models.CharField(max_length=255, null=True, blank=True)
    segment1 = models.CharField(max_length=255, null=True, blank=True)
    segment2 = models.CharField(max_length=255, null=True, blank=True)
    segment3 = models.CharField(max_length=255, null=True, blank=True)
    sku_sales_type = models.CharField(max_length=255, null=True, blank=True)
    sku_stock_type = models.CharField(max_length=255, null=True, blank=True)

    storage_capacity_area_uom = models.CharField(max_length=255, null=True, blank=True)
    storage_capacity_volume_uom = models.CharField(max_length=255, null=True, blank=True)

    aopdos = models.IntegerField(default=0)
    dos = models.IntegerField(default=0)
    manufacturing_shifts_per_day = models.IntegerField(default=0)
    msl_max = models.IntegerField(default=0)
    msl_min = models.IntegerField(default=0)
    goods_in_transit_quantity = models.FloatField(default=0.0)
    goods_pbns_quantity = models.FloatField(default=0.0)
    msl_quantity = models.FloatField(default=0.0)
    priority = models.IntegerField(default=0)
    production_capacity = models.FloatField(default=0.0)
    safety_stock_quantity = models.FloatField(default=0.0)
    sales_order_quantity = models.FloatField(default=0.0)
    share_business = models.IntegerField(default=0)
    stock_in_hand_quantity = models.FloatField(default=0.0)

    cogs_unit_price = models.IntegerField(default=0)
    manufacturing_capacity = models.IntegerField(default=0)
    manufacturing_cost_unit_price = models.IntegerField(default=0)
    manufacturing_lead_time_unit = models.IntegerField(default=0)
    nsr_unit_price = models.IntegerField(default=0)
    other_unit_price = models.IntegerField(default=0)

    picked_but_not_shipped = models.FloatField(default=0.0)
    purchase_order_quantity = models.FloatField(default=0.0)
    production_priority = models.IntegerField(default=0)
    production_sob = models.IntegerField(default=0)
    reorder_point_quantity = models.IntegerField(default=0)
    safety_stock = models.IntegerField(default=0)
    stock_in_hand = models.FloatField(default=0.0)
    stock_in_transit = models.FloatField(default=0.0)
    sales_point_quantity = models.FloatField(default=0.0)

    storage_capacity_volume = models.IntegerField(default=0)
    units_warehoused_full_utilization_day = models.FloatField(default=0.0)
    units_manufactured_full_utilization_day = models.FloatField(default=0.0)

    manufacturingShiftDay = models.JSONField(null=True, blank=True)
    manufacturing_shift_day = models.CharField(max_length=255, null=True, blank=True)
    storage_capacity_area = models.IntegerField(default=0)

    class Meta:
        db_table = "sku_node_mapping"

    def __str__(self):
        return f"SKU-Node Mapping {self.id}"
