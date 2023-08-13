import csv
import pymysql

# Database connection details
db = pymysql.connect(host="localhost", user="UNAME", password="PASSWD", database="DB_NAME")
cursor = db.cursor()

# Read data from CSV and insert into the 'menu' table
with open('menu.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        item_id, item_name, price = row
        cursor.execute("INSERT INTO menu (id, item_name, price) VALUES (%s, %s, %s)", (item_id, item_name, price))
    db.commit()
    print("Foods are now in Stock!")

# Close the database connection
db.close()
