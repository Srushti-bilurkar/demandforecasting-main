from django.urls import path
from .views import UploadSalesHistoryCSV  # ✅ Make sure the view name is correct

urlpatterns = [
    path('upload-sales-history/', UploadSalesHistoryCSV.as_view(), name='upload-sales-history'),
]
