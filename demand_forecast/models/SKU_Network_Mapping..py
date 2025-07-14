from django.db import models
import uuid

class SKUNetworkMapping(models.Model):
    sku_network_mapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()

    asset_capacity_uom = models.CharField(max_length=255, null=True, blank=True)
    asset_type = models.CharField(max_length=255, null=True, blank=True)
    asset_capacity_unit = models.FloatField(null=True, blank=True)
    carrier = models.CharField(max_length=255, null=True, blank=True)

    contract_end_date = models.DateField(null=True, blank=True)
    contract_life_cycle_status = models.BooleanField(null=True, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_sunset_date = models.DateField(null=True, blank=True)
    contract_type = models.CharField(max_length=255, null=True, blank=True)

    cycle_time_uom = models.CharField(max_length=255, null=True, blank=True)
    cycle_time_unit = models.FloatField(null=True, blank=True)

    fixed_cost = models.FloatField(null=True, blank=True)
    fixed_cost_currency = models.CharField(max_length=255, null=True, blank=True)

    ownership = models.CharField(max_length=255, null=True, blank=True)
    transporter = models.CharField(max_length=255, null=True, blank=True)

    variable_cost_currency = models.CharField(max_length=255, null=True, blank=True)
    variable_cost_unit = models.FloatField(null=True, blank=True)

    # Foreign Keys (update app_label if needed)
    mapping_mode = models.ForeignKey('MappingMode', on_delete=models.SET_NULL, null=True, blank=True)
    network = models.ForeignKey('Network', on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.ForeignKey('SKU', on_delete=models.SET_NULL, null=True, blank=True)
    channel = models.ForeignKey('Channel', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.CharField(max_length=255, null=True, blank=True)

    delivery_lead_time = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)
    share_of_business = models.FloatField(default=0.0)
    replenishment_priority = models.IntegerField(default=0)
    replenishment_share_of_business = models.IntegerField(default=0)

    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    distance_uom = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    mapping_mode_code = models.CharField(max_length=255, null=True, blank=True)

    max_order_quantity = models.FloatField(null=True, blank=True)
    max_order_value = models.FloatField(null=True, blank=True)
    min_order_quantity = models.FloatField(null=True, blank=True)
    min_order_value = models.FloatField(null=True, blank=True)

    network_code = models.CharField(max_length=255, null=True, blank=True)
    purchase_priority = models.IntegerField(null=True, blank=True)
    purchase_share_of_business = models.IntegerField(null=True, blank=True)

    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    rm_network_mapping_code = models.CharField(max_length=255, null=True, blank=True)
    sku_network_mapping_code = models.CharField(max_length=255, null=True, blank=True)
    volume_uom = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "sku_network_mapping"

    def __str__(self):
        return f"SKUNetworkMapping {self.sku_network_mapping_code or self.sku_network_mapping_id}"
