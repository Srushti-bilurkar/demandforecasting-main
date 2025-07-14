import csv
from datetime import datetime
from demand_forecast.models import Employee, Warehouse

with open("C:/Users/srush/OneDrive/Desktop/Employee.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # Clean keys and values by stripping spaces
        row = {k.strip().lower(): v.strip() for k, v in row.items()}
        
        try:
            warehouse = Warehouse.objects.get(id=row['warehouse_id'])
            
            emp, created = Employee.objects.update_or_create(
                id=row['id'],
                defaults={
                    'name': row['name'],
                    'role': row['role'],
                    'warehouse': warehouse,
                    'contact_info': row['contact_info'],
                    'hire_date': datetime.strptime(row['hire_date'], "%Y-%m-%d"),
                    'status': row['status']
                }
            )
            print(f"{'✅ Created' if created else '🔁 Updated'}: {emp.id} - {emp.name}")
        
        except Warehouse.DoesNotExist:
            print(f"⚠️ Warehouse ID {row['warehouse_id']} not found. Skipping employee {row['id']}.")
        
        except KeyError as e:
            print(f"❌ Missing column in CSV: {e}. Please check header row.")
