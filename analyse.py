#Independent Practice
def classify(area):
    if area > 9:
        return "large"
    else:
        return "small"

#Initialize running total variable   
total = 0 

with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])

#Add each ward's area to the running total
total = total + area_km2

#Call the classification function inside the loop
size = classify(area_km2)

print(ward, "is", size)

#Print the total once outside the loop
print("Total area:", total)