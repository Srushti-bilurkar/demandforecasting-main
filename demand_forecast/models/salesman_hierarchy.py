from django.db import models
import uuid

class SalesmanHierarchy(models.Model):
    salesman_hierarchy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    personnel_id = models.UUIDField()

    class Meta:
        db_table = "salesman_hierarchy"

    def __str__(self):
        return f"SalesmanHierarchy {self.name}"
