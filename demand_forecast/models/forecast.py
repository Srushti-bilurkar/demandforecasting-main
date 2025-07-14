from django.db import models
import uuid

class Forecast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    location_attribute = models.TextField(null=True, blank=True)
    operational_forecast_value = models.FloatField(null=True, blank=True)
    operational_forecast_volume = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    product_attribute = models.TextField(null=True, blank=True)
    salesmen_forecast_value = models.FloatField(null=True, blank=True)
    salesmen_forecast_volume = models.IntegerField(null=True, blank=True)
    snop_id = models.UUIDField(null=True, blank=True)
    statistical_forecast_value = models.FloatField(null=True, blank=True)
    statistical_forecast_volume = models.IntegerField(null=True, blank=True)
    unconstrained_forecast_value = models.FloatField(null=True, blank=True)
    unconstrained_forecast_volume = models.IntegerField(null=True, blank=True)
    sales_forecast_value = models.FloatField(null=True, blank=True)
    sales_forecast_volume = models.IntegerField(null=True, blank=True)
    channel = models.UUIDField(null=True, blank=True)
    node_id = models.UUIDField(null=True, blank=True)
    sku_id = models.UUIDField(null=True, blank=True)
    baseline_forecast_value = models.FloatField(null=True, blank=True)
    baseline_forecast_volume = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "forecast"

    def __str__(self):
        return f"Forecast for {self.date} | BU: {self.bu_id}"
