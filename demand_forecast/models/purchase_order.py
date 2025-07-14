from django.db import models
import uuid

class PurchaseOrder(models.Model):
    purchase_order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    actual_distance = models.FloatField(null=True, blank=True)
    actual_purchase_order_completion_date = models.DateTimeField(null=True, blank=True)
    actual_purchase_order_creation_date = models.DateTimeField(null=True, blank=True)
    actual_purchase_order_loading_date = models.DateTimeField(null=True, blank=True)
    actual_purchase_order_packing_date = models.DateTimeField(null=True, blank=True)
    actual_purchase_order_shipping_date = models.DateTimeField(null=True, blank=True)
    actual_purchase_order_unloading_date = models.DateTimeField(null=True, blank=True)

    approval_status = models.CharField(max_length=255, null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)

    batch_code = models.CharField(max_length=255, null=True, blank=True)
    batch_expiry_date = models.CharField(max_length=255, null=True, blank=True)
    batch_manufacturing_date = models.DateTimeField(null=True, blank=True)

    case_size = models.FloatField(null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)

    delivered_purchase_order_quantity = models.FloatField(null=True, blank=True)
    destination_node_code = models.CharField(max_length=255, null=True, blank=True)
    destination_stock_in_hand = models.FloatField(null=True, blank=True)
    destination_stock_in_transit = models.FloatField(null=True, blank=True)

    distance_uom = models.CharField(max_length=255, null=True, blank=True)
    fixed_shipping_cost = models.FloatField(null=True, blank=True)

    in_transit_purchase_order_quantity = models.FloatField(null=True, blank=True)
    inbound_eta = models.DateTimeField(null=True, blank=True)

    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    item_code = models.CharField(max_length=255, null=True, blank=True)
    item_cost = models.FloatField(null=True, blank=True)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)

    job_code = models.CharField(max_length=255, null=True, blank=True)
    lead_time_in_days = models.IntegerField(null=True, blank=True)
    leg_code = models.CharField(max_length=255, null=True, blank=True)
    lot_size = models.FloatField(null=True, blank=True)

    maximum_stock_level = models.CharField(max_length=255, null=True, blank=True)
    mode_of_transport = models.CharField(max_length=255, null=True, blank=True)

    modified_on = models.DateTimeField(null=True, blank=True)
    net_sales_rate = models.FloatField(null=True, blank=True)
    pending_purchase_order_quantity = models.FloatField(null=True, blank=True)
    period_duration = models.FloatField(null=True, blank=True)

    plan_code = models.CharField(max_length=255, null=True, blank=True)
    planned_distance = models.FloatField(null=True, blank=True)

    planned_purchase_order_completion_date = models.DateTimeField(null=True, blank=True)
    planned_purchase_order_creation_date = models.DateTimeField(null=True, blank=True)
    planned_purchase_order_loading_date = models.DateTimeField(null=True, blank=True)
    planned_purchase_order_packing_date = models.DateTimeField(null=True, blank=True)
    planned_purchase_order_shipping_date = models.DateTimeField(null=True, blank=True)
    planned_purchase_order_unloading_date = models.DateTimeField(null=True, blank=True)

    purchase_order_actual_delivery_date = models.DateTimeField(null=True, blank=True)
    purchase_order_actual_quantity = models.FloatField(null=True, blank=True)
    purchase_order_code = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_last_status_update_on = models.DateTimeField(null=True, blank=True)
    purchase_order_planned_delivery_date = models.DateTimeField(null=True, blank=True)
    purchase_order_planned_quantity = models.FloatField(null=True, blank=True)
    purchase_order_required_delivery_date = models.DateTimeField(null=True, blank=True)
    purchase_order_required_quantity = models.FloatField(null=True, blank=True)

    purchase_order_status = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_type = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_value = models.FloatField(null=True, blank=True)

    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    reason_code = models.CharField(max_length=255, null=True, blank=True)
    safety_stock = models.CharField(max_length=255, null=True, blank=True)
    shipment_code = models.CharField(max_length=255, null=True, blank=True)
    shipper_code = models.CharField(max_length=255, null=True, blank=True)
    shipping_type = models.CharField(max_length=255, null=True, blank=True)

    short_supply = models.FloatField(null=True, blank=True)
    source_stock_in_hand = models.FloatField(null=True, blank=True)
    source_vendor_code = models.CharField(max_length=255, null=True, blank=True)
    source_vendor_name = models.CharField(max_length=255, null=True, blank=True)

    supplier_share_of_business = models.IntegerField(null=True, blank=True)
    total_shipping_cost = models.FloatField(null=True, blank=True)
    user_remarks = models.CharField(max_length=255, null=True, blank=True)
    variable_shipping_cost = models.FloatField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=255, null=True, blank=True)

    vendor_priority = models.IntegerField(null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)
    mode_of_trans_purchase_order = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "purchase_order"

    def __str__(self):
        return self.purchase_order_code or str(self.purchase_order_id)
