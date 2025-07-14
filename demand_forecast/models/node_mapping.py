from django.db import models
import uuid

class NodeMapping(models.Model):
    node_mapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    bu_id = models.UUIDField()

    capacity_manufacturing_uom = models.CharField(max_length=255, null=True, blank=True)
    capacity_warehouse_uom = models.CharField(max_length=255, null=True, blank=True)
    capacity_warehouse_unit = models.FloatField(null=True, blank=True)

    node_lifecycle_sunset_date = models.DateField(null=True, blank=True)
    manufacturing_capacity = models.FloatField(null=True, blank=True)
    manufacturing_operating_hours_shift = models.FloatField(null=True, blank=True)
    manufacturing_shift_day = models.CharField(max_length=255, null=True, blank=True)
    manufacturing_shifts_per_day = models.FloatField(null=True, blank=True)

    node_lifecycle_end_date = models.DateField(null=True, blank=True)
    node_lifecycle_start_date = models.DateField(null=True, blank=True)
    node_lifecycle_status = models.BooleanField()

    warehouse_operating_hours_shift = models.FloatField(null=True, blank=True)
    warehouse_shift_days = models.CharField(max_length=255, null=True, blank=True)
    warehouse_shift_per_day = models.FloatField(null=True, blank=True)

    node_id = models.UUIDField(null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    node_level = models.CharField(max_length=255, null=True, blank=True)
    node_status = models.CharField(max_length=255, null=True, blank=True)

    storage_capacity_area_uom = models.CharField(max_length=255, null=True, blank=True)
    internal_external_node = models.CharField(max_length=255, null=True, blank=True)
    warehouse_volume_capacity = models.FloatField(null=True, blank=True)
    warehouse_volume_capacity_uom = models.CharField(max_length=255, null=True, blank=True)

    warehouse_loading_shift = models.JSONField(null=True, blank=True)
    warehouse_unloading_shift = models.JSONField(null=True, blank=True)
    working_days = models.JSONField(null=True, blank=True)
    planning_days = models.JSONField(null=True, blank=True)
    operating_hours_shift = models.JSONField(null=True, blank=True)

    contact_number = models.BigIntegerField(default=0)
    storage_capacity_area = models.BigIntegerField(default=0)
    warehouse_volume_capacity_value = models.FloatField(default=0.0)

    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    volume_uom = models.CharField(max_length=255, null=True, blank=True)
    overall_node_yield = models.IntegerField(default=0)
    overall_node_equipment_effectiveness = models.IntegerField(default=0)

    class Meta:
        db_table = "node_mapping"

    def __str__(self):
        return f"NodeMapping {self.node_mapping_id}"
