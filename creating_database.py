import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('datamart.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price REAL,
        inventory INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")