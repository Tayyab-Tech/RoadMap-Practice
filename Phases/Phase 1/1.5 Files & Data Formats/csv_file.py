# CSV = Comma Separated Values
# Example
# Name,Age,City
# Ali,20,Lahore
# Sara,22,Karachi
# Each row represents a record.
# Each comma separates columns.
import csv

rows = [
    ["Ali", 20,"lahore"],
    ["Ahmed", 30,"ISL"],
    ["Sara", 21,"NULL"]
]
with open("Phase 1\\1.5 Files & Data Formats\\students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerows(rows)

with open("Phase 1\\1.5 Files & Data Formats\\students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("Phase 1\\1.5 Files & Data Formats\\students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# Important CSV Methods
# csv.reader()
# csv.writer()
# csv.DictReader()
# csv.DictWriter()
# writerow()
# writerows()
# writeheader()