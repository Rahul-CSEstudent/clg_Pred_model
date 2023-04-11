import json
import csv

with open ("engineering.csv", "r") as f:
    reader = csv.DictReader(f)
    next(reader)
    data = { }
    i =0
    for rows in reader:

        key = rows['tlr']
        data[key] = rows
        
with open ("college.json", "w") as f:
    json.dump(data, f, indent=4)
