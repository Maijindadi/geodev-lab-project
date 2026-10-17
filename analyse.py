with open("wards.csv", "r") as f:
    lines = f.readlines()

print("number of lines:", len(lines))

with open ("wards.csv") as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())

with open ("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    wards = parts[0]
    area = parts[1]
    print(wards, "has area", area)

with open ("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    wards = parts[0]
    area_km2 = float(parts[1])
    area_ha = area_km2 * 100
    print(wards, "is", area_ha, "hectares")

with open ("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    wards = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(wards, "is", size)


with open ("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    wards = parts[0]
    area_km2 = float(parts[1])