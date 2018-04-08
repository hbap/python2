"""
Gets a stock quote.

Demonstrates an HTTP API.
"""

import csv
import os
import requests
import sys

# Check for symbol
if len(sys.argv) != 2:
    sys.exit("Usage: python3 quote.py SYMBOL")
symbol = sys.argv[1]

# Get API_KEY
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    sys.exit("Missing API_KEY")

# Get data as a CSV file
url = f"https://www.alphavantage.co/query?apikey={API_KEY}&datatype=csv&function=TIME_SERIES_INTRADAY&interval=1min&symbol={symbol}"
response = requests.get(url)

# Parse CSV
reader = csv.DictReader(response.text.splitlines())

# Print most recent price
row = next(reader)
print(f"${row['close']}")
