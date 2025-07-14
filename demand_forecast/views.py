# demand_forecast/views.py
import csv
import uuid
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SalesHistory

class UploadSalesHistoryCSV(APIView):
    def post(self, request):
        csv_path = request.data.get("csv_path")

        if not csv_path:
            return Response({"error": "CSV path not provided."}, status=400)

        try:
            with open(csv_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                chunk = []
                for i, row in enumerate(reader):
                    try:
                        chunk.append(SalesHistory(
                            id=uuid.uuid4(),
                            bu_id=uuid.uuid4(),
                            created_at=datetime.now(),
                            created_by=uuid.uuid4(),
                            modified_at=datetime.now(),
                            modified_by=uuid.uuid4(),
                            tenant_id=uuid.uuid4(),

                            date=row.get('date'),

                            salesman_name=row.get('salesman_name'),
                            actual_sales_value=float(row['actual_sales_value']) if row.get('actual_sales_value') else None,
                            actual_sales_volume=int(row['actual_sales_volume']) if row.get('actual_sales_volume') else None,
                            cleaned_sales_value=float(row['cleaned_sales_value']) if row.get('cleaned_sales_value') else None,
                            net_value=float(row['net_value']) if row.get('net_value') else None,
                            promo_type=row.get('promo_type'),
                            unit_selling_price=float(row['unit_selling_price']) if row.get('unit_selling_price') else None
                        ))

                        if len(chunk) == 100:
                            SalesHistory.objects.bulk_create(chunk)
                            chunk = []

                    except Exception as e:
                        print(f"Row {i+1} skipped due to error: {e}")

                if chunk:
                    SalesHistory.objects.bulk_create(chunk)

            return Response({"message": "CSV data uploaded successfully!"}, status=201)

        except FileNotFoundError:
            return Response({"error": "CSV file not found."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
