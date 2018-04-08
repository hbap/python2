"""
Prints employees' names.

Demonstrates a list comprehension and sorting by a key.
"""

import csv
import sys

def birthdate(e):
    return e["BirthDate"]

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees4.py FILE")

# Import employees
with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    employees = [row for row in reader]

# Sort employees by birthdate
for employee in sorted(employees, key=birthdate):
    print(employee["FirstName"], employee["LastName"], employee["BirthDate"])
