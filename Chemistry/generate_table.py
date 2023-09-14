import csv
import json

head = ["name", "weight", "charges", "type", "phase", "melting", "boiling"]
dict = {}
with open("periodic.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for r in row:
            if r == "None":
                r = None

        tmp = [row[3]] + row[1:3] + row[4::3] + row[5:7]
        dict[row[0]] = {x:y for x,y in zip(head, tmp)}

with open("ptable.json", "w") as jsonfile:
    json.dump(dict, jsonfile)