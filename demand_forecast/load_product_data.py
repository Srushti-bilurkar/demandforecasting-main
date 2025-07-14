import csv
from demand_forecast.models import Product, Category, Supplier

with open("C:/Users/srush/OneDrive/Desktop/Product.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Normalize header keys (make all lowercase)
        row = {k.strip().lower(): v.strip() for k, v in row.items()}
        try:
            category = Category.objects.get(id=row['category_id'])
            supplier = Supplier.objects.get(id=row['supplier_id'])

            product, created = Product.objects.update_or_create(
                sku=row['sku'],
                defaults={
                    'name': row['name'],
                    'description': row['description'],
                    'category': category,
                    'unit_price': float(row['unit_price']),
                    'weight': float(row['weight']),
                    'dimensions': row['dimensions'],
                    'reorder_level': int(row['reorder_level']),
                    'reorder_quantity': int(row['reorder_quantity']),
                    'supplier': supplier
                }
            )
            print(f"{'✅ Created' if created else '🔁 Updated'}: {product.sku} - {product.name}")
        
        except Category.DoesNotExist:
            print(f"❌ Category ID {row['category_id']} not found for SKU {row['sku']}")
        except Supplier.DoesNotExist:
            print(f"❌ Supplier ID {row['supplier_id']} not found for SKU {row['sku']}")
