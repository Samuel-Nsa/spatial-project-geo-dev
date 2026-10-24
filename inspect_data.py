import csv

def inspect_column(filename, column):
    values = []
    non_numeric_count = 0

    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        for row in rows:
            raw = row[column].strip()
            if raw == "":
                continue
            
            # Try converting to float; count as non-numeric if it fails
            try:
                values.append(float(raw))
            except ValueError:
                non_numeric_count += 1

    # Guard against empty/invalid numeric lists (ZeroDivisionError protection)
    if not values:
        return {
            "status": "No valid numeric data found",
            "non_numeric_count": non_numeric_count,
            "count": 0
        }

    # Calculate metrics safely
    mean_val = sum(values) / len(values)

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": round(mean_val, 2),
        "non_numeric_count": non_numeric_count
    }

# Run the function on your dataset
area_results = inspect_column("mydata.csv", "area_km2")
pop_results = inspect_column("mydata.csv", "population")

print("Area:", area_results)
print("Population:", pop_results)