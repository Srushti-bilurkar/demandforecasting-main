from django.db import models
import uuid
from .sku import SKU
from .node_mapping import NodeMapping
from .shipment import Shipment  # Assuming shipment_id will be used

class StockTransferOrder(models.Model):
    stock_transfer_order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    actual_delivery_date = models.DateField(null=True, blank=True)
    actual_distance = models.FloatField(default=0.0)
    actual_quantity = models.FloatField(default=0.0)

    actual_sto_completion_date = models.DateField(null=True, blank=True)
    actual_sto_creation_date = models.DateField(null=True, blank=True)
    actual_sto_loading_date = models.DateField(null=True, blank=True)
    actual_sto_packing_date = models.DateField(null=True, blank=True)
    actual_sto_shipping_date = models.DateField(null=True, blank=True)
    actual_sto_unloading_date = models.DateField(null=True, blank=True)

    approved_by = models.CharField(max_length=255, null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)
    batch_expiry_date = models.DateField(null=True, blank=True)
    batch_id = models.CharField(max_length=255, null=True, blank=True)
    batch_code = models.CharField(max_length=255, null=True, blank=True)
    batch_manufacturing_date = models.DateField(null=True, blank=True)
    cancelled_on = models.DateField(null=True, blank=True)

    case_size = models.IntegerField(default=0)
    container_id = models.CharField(max_length=255, null=True, blank=True)
    container_code = models.CharField(max_length=255, null=True, blank=True)

    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    demand_forecast = models.FloatField(default=0.0)

    destination_sih = models.FloatField(default=0.0)
    destination_sit = models.FloatField(default=0.0)
    destination_so_quantity = models.FloatField(default=0.0)
    destination_stock_in_hand = models.FloatField(default=0.0)
    destination_stock_in_transit = models.FloatField(default=0.0)

    distance_uom = models.CharField(max_length=255, null=True, blank=True)
    fixed_shipping_cost = models.FloatField(default=0.0)
    inbound_eta = models.DateField(null=True, blank=True)

    item_cost = models.FloatField(default=0.0)
    job_id = models.CharField(max_length=255, null=True, blank=True)
    job_code = models.CharField(max_length=255, null=True, blank=True)

    leg = models.CharField(max_length=255, null=True, blank=True)
    leg_code = models.CharField(max_length=255, null=True, blank=True)

    lot_size = models.FloatField(default=0.0)
    max_stock_level = models.FloatField(default=0.0)
    mode = models.CharField(max_length=255, null=True, blank=True)
    mode_of_transport = models.CharField(max_length=255, null=True, blank=True)

    net_sales_rate = models.FloatField(default=0.0)
    period = models.CharField(max_length=255, null=True, blank=True)
    plan_id = models.CharField(max_length=255, null=True, blank=True)
    plan_code = models.CharField(max_length=255, null=True, blank=True)

    planned_delivery_date = models.DateField(null=True, blank=True)
    planned_distance = models.FloatField(default=0.0)
    planned_quantity = models.FloatField(default=0.0)

    planned_sto_completion_date = models.DateField(null=True, blank=True)
    planned_sto_creation_date = models.DateField(null=True, blank=True)
    planned_sto_loading_date = models.DateField(null=True, blank=True)
    planned_sto_packing_date = models.DateField(null=True, blank=True)
    planned_sto_shipping_date = models.DateField(null=True, blank=True)
    planned_sto_unloading_date = models.DateField(null=True, blank=True)

    priority = models.IntegerField(default=0)

    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    reason_code = models.CharField(max_length=255, null=True, blank=True)

    required_delivery_date = models.DateField(null=True, blank=True)
    required_quantity = models.FloatField(default=0.0)
    safety_stock = models.FloatField(default=0.0)

    short_supply = models.IntegerField(default=0)
    shipment_code = models.CharField(max_length=255, null=True, blank=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)

    shipper = models.CharField(max_length=255, null=True, blank=True)
    shipper_code = models.CharField(max_length=255, null=True, blank=True)
    shipping_type = models.CharField(max_length=255, null=True, blank=True)

    sku_code = models.ForeignKey(SKU, on_delete=models.CASCADE, null=True, blank=True)
    sku_name = models.CharField(max_length=255, null=True, blank=True)

    source_sih = models.FloatField(default=0.0)
    source_stock_in_hand = models.FloatField(default=0.0)
    source_node = models.ForeignKey(NodeMapping, related_name='sto_source_node', on_delete=models.SET_NULL, null=True, blank=True)
    destination_node = models.ForeignKey(NodeMapping, related_name='sto_dest_node', on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(max_length=255, null=True, blank=True)
    sto_id = models.CharField(max_length=255, null=True, blank=True)
    sto_status = models.CharField(max_length=255, null=True, blank=True)
    sto_type = models.CharField(max_length=255, null=True, blank=True)
    sto_value = models.FloatField(default=0.0)

    user_remarks = models.CharField(max_length=255, null=True, blank=True)
    variable_shipping_cost = models.FloatField(default=0.0)

    vehicle_id = models.CharField(max_length=255, null=True, blank=True)
    vehicle_code = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)

    approval_status = models.CharField(max_length=255, null=True, blank=True)
    delivered_sto_quantity = models.FloatField(default=0.0)
    in_transit_sto_quantity = models.FloatField(default=0.0)
    pending_sto_quantity = models.FloatField(default=0.0)

    sto_code = models.CharField(max_length=255, unique=True)
    sto_last_update_status_on = models.DateField(null=True, blank=True)

    lead_time_in_days = models.IntegerField(default=0)

    class Meta:
        db_table = "stock_transfer_order"

    def __str__(self):
        return f"STO {self.sto_code}"
