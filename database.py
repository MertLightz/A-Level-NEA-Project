import sqlite3
from tkinter import *

# Connect to database
connector = sqlite3.connect('shop.db')

# Create a cursor
cursor = connector.cursor()

'''
# Create a table
cursor.execute("""CREATE TABLE chocolates (
        product_name text,
        stock integer
    )""")
    # Datatypes:
    # NULL - doesn't exist
    # INTEGER - whole number
    # REAL - decimal number
    # TEXT - string
    # BLOB - stored exactly as it is
'''

'''
# Insert one record at a time
cursor.execute("INSERT INTO chocolates VALUES ('Crunchie', 5)")
'''

'''
# Insert multiple records at a time
multiple_products = [
                        ('Dairy Milk', 5), 
                        ('KitKat', 5), 
                        ('Kinder Bueno', 5)
                    ]
cursor.executemany("INSERT INTO chocolates VALUES (?,?)", multiple_products)
'''

'''
# Query the database
cursor.execute("SELECT * FROM chocolates")

    # Ways to fetch:
    # fetchone() - Last item in the table
    # fetchmany(2) - Certain number of items
    # fetchall() - All items

print(cursor.fetchall())
'''

# Push changes to the database
connector.commit()

# Close connection
connector.close()

root = Tk()
root.title('STOCK CONTROL SYSTEM')