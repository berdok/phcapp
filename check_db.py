import sqlite3

# Connect to the database
conn = sqlite3.connect('buyers.db')
cursor = conn.cursor()

# Fetch all rows from the 'buyers' table
cursor.execute("SELECT * FROM buyers")
rows = cursor.fetchall()

# Print out the data
for row in rows:
    print(row)

# Close the connection
conn.close()
