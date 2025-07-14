from django.db import models
import uuid

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    no_of_legs_planned = models.IntegerField(null=True, blank=True)
    actual_leg_info = models.CharField(max_length=255, null=True, blank=True)
    container_count = models.IntegerField(null=True, blank=True)
    container_list = models.CharField(max_length=255, null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    end_node_code = models.CharField(max_length=255, null=True, blank=True)
    planned_leg_info = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_count = models.IntegerField(null=True, blank=True)
    purchase_order_list = models.CharField(max_length=255, null=True, blank=True)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    raw_material_procurement_order_count = models.IntegerField(null=True, blank=True)
    raw_material_procurement_order_list = models.CharField(max_length=255, null=True, blank=True)
    route_code = models.CharField(max_length=255, null=True, blank=True)
    sales_order_count = models.IntegerField(null=True, blank=True)
    sales_order_list = models.CharField(max_length=255, null=True, blank=True)
    shipment_code = models.CharField(max_length=255, null=True, blank=True)
    shipment_status = models.CharField(max_length=255, null=True, blank=True)
    shipment_sub_status = models.CharField(max_length=255, null=True, blank=True)
    shipment_volume = models.CharField(max_length=255, null=True, blank=True)
    shipper_code = models.CharField(max_length=255, null=True, blank=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    start_node_code = models.CharField(max_length=255, null=True, blank=True)
    stock_transfer_order_count = models.IntegerField(null=True, blank=True)
    stock_transfer_order_list = models.CharField(max_length=255, null=True, blank=True)
    total_estimated_time = models.FloatField(null=True, blank=True)
    total_shipment_quantity = models.FloatField(null=True, blank=True)
    total_shipment_value = models.FloatField(null=True, blank=True)
    volume_uom = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "shipment"

    def __str__(self):
        return f"Shipment {self.shipment_code or self.id}"
