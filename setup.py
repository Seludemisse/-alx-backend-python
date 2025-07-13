import seed

# Step 1: Connect to MySQL Server and create database
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    print(" Database created (if it didn't exist).")
    connection.close()
else:
    print(" Failed to connect to MySQL server.")

# Step 2: Connect to the new database and create table + insert data
connection = seed.connect_to_prodev()
if connection:
    seed.create_table(connection)
    seed.insert_data(connection, 'user_data.csv')
    print(" Table created and data inserted.")
    connection.close()
else:
    print(" Failed to connect to ALX_prodev database.")
