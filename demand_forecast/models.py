# from django.db import models

# class Category(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., CAT001
#     name = models.CharField(max_length=100)
#     description = models.TextField()

# class Supplier(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., SUP001
#     name = models.CharField(max_length=100)
#     contact_info = models.TextField()
#     address = models.TextField()
#     lead_time = models.IntegerField()
#     status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

# class Customer(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., CUST001
#     name = models.CharField(max_length=100)
#     contact_info = models.TextField()
#     billing_address = models.TextField()
#     shipping_address = models.TextField()
#     credit_limit = models.DecimalField(max_digits=12, decimal_places=2)
#     status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

# class Warehouse(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., WH001
#     name = models.CharField(max_length=100)
#     location = models.TextField()
#     capacity = models.IntegerField()
#     status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
#     manager = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL, related_name='managed_warehouses')

# class Employee(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., EMP001
#     name = models.CharField(max_length=100)
#     role = models.CharField(max_length=50)
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='employees')
#     contact_info = models.TextField()
#     hire_date = models.DateField()
#     status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

# class Bin(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., BIN001
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='bins')
#     zone = models.CharField(max_length=20)
#     aisle = models.CharField(max_length=20)
#     rack = models.CharField(max_length=20)
#     shelf = models.CharField(max_length=20)
#     capacity = models.IntegerField()
#     status = models.CharField(max_length=20, choices=[('Occupied', 'Occupied'), ('Empty', 'Empty')])

# class Product(models.Model):
#     sku = models.CharField(primary_key=True, max_length=100)  # using SKU as primary key
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     weight = models.DecimalField(max_digits=8, decimal_places=2)
#     dimensions = models.CharField(max_length=50)
#     reorder_level = models.IntegerField()
#     reorder_quantity = models.IntegerField()
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

# class Inventory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     quantity_on_hand = models.IntegerField()
#     quantity_reserved = models.IntegerField()
#     last_updated = models.DateTimeField(auto_now=True)
#     bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

#     @property
#     def quantity_available(self):
#         return self.quantity_on_hand - self.quantity_reserved

# class Order(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., ORD001
#     ORDER_TYPES = [
#         ('Sales Order', 'Sales Order'),
#         ('Purchase Order', 'Purchase Order'),
#         ('Transfer Order', 'Transfer Order')
#     ]
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Processing', 'Processing'),
#         ('Shipped', 'Shipped'),
#         ('Delivered', 'Delivered'),
#         ('Cancelled', 'Cancelled')
#     ]
#     order_type = models.CharField(max_length=30, choices=ORDER_TYPES)
#     customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
#     supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL)
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     order_date = models.DateField()
#     expected_delivery_date = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2)

# class OrderLine(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., ORDL001
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_lines')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

#     @property
#     def total_price(self):
#         return self.quantity * self.unit_price

# class StockMovement(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., MOV001
#     MOVEMENT_TYPES = [
#         ('Inbound', 'Inbound'),
#         ('Outbound', 'Outbound'),
#         ('Transfer', 'Transfer'),
#         ('Adjustment', 'Adjustment')
#     ]
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     from_bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name='from_movements')
#     to_bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name='to_movements')
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
#     movement_date = models.DateField()
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

# class Shipment(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)  # e.g., SHIP001
#     SHIPMENT_STATUS = [
#         ('In Transit', 'In Transit'),
#         ('Delivered', 'Delivered'),
#         ('Delayed', 'Delayed')
#     ]
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     carrier_name = models.CharField(max_length=100)
#     tracking_number = models.CharField(max_length=100)
#     shipment_date = models.DateField()
#     delivery_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=20, choices=SHIPMENT_STATUS)
