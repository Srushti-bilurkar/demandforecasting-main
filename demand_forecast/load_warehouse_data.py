import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supplychain_lstm.settings')  # ✅ Use your actual project name
django.setup()

# Import your model
from demand_forecast.models import Warehouse, Employee

def load_warehouse_data():
    # ✅ Use your actual CSV path
    csv_path = r'C:\Users\srush\Downloads\Warehouse_data.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        manager = None
        if pd.notna(row['ManagerID (FK)']):
            try:
                manager = Employee.objects.get(id=row['ManagerID (FK)'])
            except Employee.DoesNotExist:
                print(f"⚠️ Manager {row['ManagerID (FK)']} not found.")

        Warehouse.objects.update_or_create(
            id=row['WarehouseID (PK)'],
            defaults={
                'name': row['Name'],
                'location': row['Location'],
                'capacity': row['Capacity'],
                'status': row['Status'],
                'manager': manager
            }
        )

    print("✅ Warehouse data loaded successfully.")

if __name__ == '__main__':
    load_warehouse_data()
