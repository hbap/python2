"""
Prints employees' names.

Demonstrates a lambda function.
"""

import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees5.py FILE")

# Import employees
with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    employees = [row for row in reader]

# Sort employees by birthdate
for employee in sorted(employees, key=lambda e: e["BirthDate"]):
    print(employee["FirstName"], employee["LastName"], employee["BirthDate"])
