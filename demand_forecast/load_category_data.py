import csv
from demand_forecast.models import Category

with open("C:/Users/srush/OneDrive/Desktop/Category.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Normalize keys
        row = {k.strip().lower(): v.strip() for k, v in row.items()}

        category, created = Category.objects.update_or_create(
            id=row["id"],
            defaults={
                "name": row["name"],
                "description": row["description"]
            }
        )
        print(f"{'✅ Created' if created else '🔁 Updated'}: {category.id} - {category.name}")
