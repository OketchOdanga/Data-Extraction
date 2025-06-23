import sqlite3
conn = sqlite3.connect('datamart.db')
cursor = conn.cursor()
for row in cursor.execute(" SELECT * FROM products"):
    print(row)
conn.commit()
