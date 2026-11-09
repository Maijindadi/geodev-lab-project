import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_rows(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue 
            values.append(float(raw))
        return values 
def summarise(values): 
    if len(values) == 0:
        return {"count": 0, "smallest": None, "Largest": None, "Average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values)
    }

def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_rows(rows, column)
        report[column] = summarise(values)  
report = summarise_all("mytree_partial_heights.csv", ["DBH", "height"])

for column, stats in report.items():
    print(column, "->", stats)
