"""
Prints employees' average age.

Demonstrates pandas and NumPy.
"""

import numpy as np
import pandas as pd
import sys

from datetime import date, datetime

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees6.py FILE")

# Import employees
df = pd.read_csv(sys.argv[1])

# Get today's date
now = datetime.now()

# Convert birthdates to ages
birthdates = []
for birthdate in df.loc[:, "BirthDate"]:
    age = now - datetime.strptime(birthdate, "%Y-%m-%d %H:%M:%S")
    birthdates.append(age.days // 365)

# Print average age
print(int(np.round(np.mean(birthdates))))
