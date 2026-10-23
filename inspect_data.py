import csv

with open ("mytree.csv", encoding ="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print("Number of rows:", len(rows))
print("Columns:", list(rows[0].keys()))


with open ("mytree.csv", encoding ="utf-8-sig") as f:
    reader = csv.DictReader(f)

values = []
for row in rows:
    value = float(row["DBH"])
    values.append(value)

print("smallest value:", min(values))
print("largest value:", max(values))
print("Count value:", len(values))


with open ("mytree.csv", encoding ="utf-8-sig") as f:
    reader = csv.DictReader(f)

values = []
for row in rows:
    raw = row["DBH"].strip()
    if raw == "":
        continue 
    values.append(float(raw))

print("smallest value:", min(values))
print("largest value:", max(values))
print("Count value:", len(values))

def inspect_column(filename, column): 
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue 
        values.append(float(raw))
    return {
        "smallest value": min(values),
        "largest value": max(values),
        "Count value": len(values),
    }

result = inspect_column("mytree_partial_heights.csv", "DBH")
print(result)

DBH_result = inspect_column("mytree_partial_heights.csv", "DBH")
height_result = inspect_column("mytree_partial_heights.csv", "height")

print("DBH result:", DBH_result)
print("height result:", height_result)