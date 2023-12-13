# This file converts a CSV file into a db file, I had started trying to implement it locally but ran into issues and used the web platform instead.

# Import needed libraries
import csv
import sqlite3
import os

# Function: CSV [Input] to DB [Output]
def csv_to_sqlite(csv_file, db_file, table_name):

    # File path from folders
    csv_file_path = os.path.join('data_csv', csv_file) # Existing CSV File
    db_file_path = os.path.join('database_db', db_file) # New DB File

    # Improved: Error Handling & Connection to SQLite database
    # CS50 handles this with db = SQL(...) for - grateful for those training wheels
    try:
        path = sqlite3.connect(db_file_path)
        cursor = path.cursor()

    except sqlite3.Error as error:
        print(f"An error occurred: {error}")

    # Using CSV info to create DB Table - scans one column at a time into memory
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        columns = ', '.join(header)
        placeholders = ', '.join('?' * len(header))
        createTable = f'CREATE TABLE {table_name} ({columns})'
        cursor.execute(createTable)

        # Insert data into table
        for row in reader:
            cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)

    # Commit and close connection to PATH
    # CS50 handles this with - from cs50 import SQL
    path.commit()
    path.close()
    print(f"CSV data from '{csv_file}' imported to '{db_file}' as table '{table_name}'.")


# Function call using my files / names
csv_to_sqlite('sports_dataset.csv', 'sports.db', 'sports_table')
