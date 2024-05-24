# setup_db.py
import sqlite3
import csv

conn = sqlite3.connect('foodtrucks.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS foodtrucks (
    id INTEGER PRIMARY KEY,
    name TEXT,
    latitude REAL,
    longitude REAL
)
''')

with open('food-truck-data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        name = row[1]
        latitude = row[14]
        longitude = row[15]

        cursor.execute('INSERT INTO foodtrucks (name, latitude, longitude) VALUES (?, ?, ?)', (name, latitude, longitude))
conn.commit()
conn.close()
