# Create a connection for DB and print the version using a python program
import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)
print(mydb) 

cursor = mydb.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
mydb.close()

print("Python version : ",sys.version)
#Output:-
#<mysql.connector.connection_cext.CMySQLConnection object at 0x0000026FD2007F88>
#Database version : 8.0.25 
#Python version :  3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]


# Create a multiple tables & insert data in table

import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)

cur = db.cursor()
cur.execute("CREATE TABLE customer(name VARCHAR(255), address VARCHAR(255))")
cur.execute("CREATE TABLE student(First_name VARCHAR(255),Last_name VARCHAR(255), Age int)")
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cur.execute(sql, val)

db.commit()

print(cur.rowcount, "record inserted.")

sql = "INSERT INTO student (First_name,Last_name, Age) VALUES (%s, %s, %s)"
val = ("Monkey D", "Luffy", "21")
cur.execute(sql, val)

db.commit()

print(cur.rowcount, "record inserted.")

#Output:-
#1 record inserted.
#1 record inserted.


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Output
#('customer',)
#('student',)
  
# Create a employee table and read all the employee name in the table using for loop

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Output:-
#('John', 'Highway 21')
#('Monkey D', 'Luffy', 21)
