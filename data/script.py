import csv
import json

# Input & output file names
csv_file = 'codes.csv'
json_file = 'codes.json'

# Initialize an empty list to hold the data
csv_data_list = []

# Read the CSV file
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Get the headers (field names)
    headers = next(csvreader)

    # Check if the CSV file has exactly two fields
    if len(headers) != 2:
        print("The CSV file must have exactly two fields.")
        exit()

    # Read each row and append it as a dictionary to the list
    for row in csvreader:
        csv_data_list.append({headers[0]: row[0], headers[1]: row[1]})

# Write to JSON file
with open(json_file, 'w') as jsonfile:
    json.dump(csv_data_list, jsonfile, indent=4)

print(f"Data has been written to {json_file}")
