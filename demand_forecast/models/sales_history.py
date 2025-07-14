from django.db import models
import uuid

class SalesHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_id = models.UUIDField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField()
    modified_at = models.DateTimeField()
    modified_by = models.UUIDField()
    tenant_id = models.UUIDField()

    actual_sales_value = models.FloatField(null=True, blank=True)
    actual_sales_value_uom = models.TextField(null=True, blank=True)
    actual_sales_volume = models.IntegerField(null=True, blank=True)
    actual_sales_volume_uom = models.TextField(null=True, blank=True)

    adjusted_sales_value = models.FloatField(null=True, blank=True)
    adjusted_sales_value_uom = models.TextField(null=True, blank=True)
    adjusted_sales_volume = models.IntegerField(null=True, blank=True)
    adjusted_sales_volume_uom = models.TextField(null=True, blank=True)

    cleaned_sales_value = models.FloatField(null=True, blank=True)
    cleaned_sales_value_uom = models.TextField(null=True, blank=True)
    cleaned_sales_volume = models.IntegerField(null=True, blank=True)
    cleaned_sales_volume_uom = models.TextField(null=True, blank=True)

    date = models.DateField()
    salesman_email_address = models.TextField(null=True, blank=True)
    salesman_name = models.TextField(null=True, blank=True)
    channel = models.UUIDField(null=True, blank=True)
    node_id = models.UUIDField(null=True, blank=True)
    sku_id = models.UUIDField(null=True, blank=True)

    actual_dispatch_date = models.DateField(null=True, blank=True)
    area_id = models.TextField(null=True, blank=True)
    area_sales_executive = models.TextField(null=True, blank=True)
    branch_incharge = models.TextField(null=True, blank=True)
    customer_classification = models.TextField(null=True, blank=True)
    customer_group = models.TextField(null=True, blank=True)
    customer_id = models.TextField(null=True, blank=True)
    customer_name = models.TextField(null=True, blank=True)
    divisional_sales_head = models.TextField(null=True, blank=True)

    gst_amount = models.FloatField(null=True, blank=True)
    gst_percentage = models.FloatField(null=True, blank=True)
    invoice_number = models.BigIntegerField(null=True, blank=True)
    net_value = models.FloatField(null=True, blank=True)

    order_book_date = models.DateField(null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    order_status = models.CharField(max_length=255, null=True, blank=True)
    promo_description = models.TextField(null=True, blank=True)
    promo_id = models.IntegerField(null=True, blank=True)
    promo_type = models.TextField(null=True, blank=True)
    requested_delivery_date = models.DateField(null=True, blank=True)
    so_number = models.TextField(null=True, blank=True)

    tax_amount = models.FloatField(null=True, blank=True)
    unit_selling_price = models.FloatField(null=True, blank=True)
    order_booked_date = models.DateField(null=True, blank=True)
    on_hand_quantity = models.FloatField(null=True, blank=True)
    open_quantity = models.FloatField(null=True, blank=True)
    promo_free_quantity = models.IntegerField(null=True, blank=True)

    area_code = models.TextField(null=True, blank=True)
    branch_incharge_code = models.TextField(null=True, blank=True)
    cost_uom = models.CharField(max_length=255, null=True, blank=True)
    customer_code = models.TextField(null=True, blank=True)
    divisional_sales_head_code = models.TextField(null=True, blank=True)
    quantity_uom = models.CharField(max_length=255, null=True, blank=True)
    sales_order_number = models.TextField(null=True, blank=True)
    volume_uom = models.CharField(max_length=255, null=True, blank=True)

    delivered_order_quantity = models.FloatField(default=0.0)
    pending_order_quantity = models.FloatField(default=0.0)
    in_transit_order_quantity = models.FloatField(default=0.0)
    promo_code = models.IntegerField(default=0)

    class Meta:
        db_table = "sales_history"

    def __str__(self):
        return f"SalesHistory {self.id}"
