import seed

connection = seed.connect_to_prodev()

if connection:
    print("Streaming rows one by one using generator:\n")

    for row in seed.stream_user_data(connection):
        print(row)

    connection.close()
else:
    print("Failed to connect to ALX_prodev database.")
