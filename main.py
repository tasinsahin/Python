import csv
from datetime import datetime
from tabulate import tabulate

with open('findik2.csv', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Create a list of columns to keep
columns_to_keep = ["dt", "temp"]

# Create a new list of dictionaries containing only the desired columns
filtered_data = []
for row in data:
    filtered_row = {col: row[col] for col in columns_to_keep}
    filtered_data.append(filtered_row)

for row in filtered_data:
    if 'dt' in row:
        timestamp = int(row['dt'])
        dt_utc = datetime.utcfromtimestamp(timestamp)
        row['dt'] = dt_utc

# Convert the list of dictionaries to a list of lists for tabulate
table_data = []
for row in filtered_data:
    table_data.append([row["dt"], row["temp"]])

# Define the table headers
headers = ["Timestamp (UTC)", "Temperature"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))
