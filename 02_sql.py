# INSERT Command

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('NYC','NY',8400000)")
cursor.execute("INSERT INTO population VALUES('San Fran','CA',80000)")

# commit the changes
conn.commit()

# close connection
conn.close()
