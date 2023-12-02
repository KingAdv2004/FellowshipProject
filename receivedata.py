import sqlite3

# Retrieve data from the table
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(f"name: {row[0]}, email: {row[1]}, password: {row[2]}")

# Close the connection
conn.close()
exit()