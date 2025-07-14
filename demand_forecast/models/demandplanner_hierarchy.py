import uuid
from django.db import models

class DemandPlannerHierarchy(models.Model):
    demandplannerhierarchy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    personnel_id = models.UUIDField()

    class Meta:
      db_table = "demandplanner_hierarchy"
      indexes = [
          models.Index(fields=['personnel_id'], name='idx_dph_pid'),  # shortened index name
    ]


    def __str__(self):
        return self.name or str(self.demandplannerhierarchy_id)
