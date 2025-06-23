# Extracting Data from the CSV File
import csv

# Open the CSV file
with open('products.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    header = next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        print(row)

