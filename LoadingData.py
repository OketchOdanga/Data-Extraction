import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect('datamart.db')
cursor = conn.cursor()

# Open the CSV file
with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in reader:
        try:
            product_id = int(row[0])
            product_name = row[1]
            category = row[2]
            price = float(row[3])
            inventory = int(row[4])

            # Insert the data into the products table
            cursor.execute('''
                INSERT OR REPLACE INTO products (product_id, product_name, category, price, inventory)
                VALUES (?, ?, ?, ?, ?)
            ''', (product_id, product_name, category, price, inventory))
        except ValueError as e:
            print(f"Skipping row due to data type error: {row} - {e}")


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data loaded successfully!")