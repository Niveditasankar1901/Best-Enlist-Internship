# Day-18
#1-Create a DB with doctor and doctor ID & patients visited
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98"
)

cur = db.cursor()
cur.execute("CREATE DATABASE doctor")

cur = db.cursor()
cur.execute("USE doctor")
cur.execute("CREATE TABLE doctor_details( Id INT PRIMARY KEY,Name VARCHAR(255) , patients_visited INT)")
sql = "INSERT INTO doctor_details (Id ,Name,patients_visited) VALUES (%s,%s, %s)"
val = [
    ("1", "Chopper","10"),
    ("2", "Genos","0"),
    ("3", "Mob","2"),
    ("4", "Kakashi", "20")
    ]
cur.executemany(sql, val)

db.commit()

print(cur.rowcount, "was inserted.")
#Output:-
#4 was inserted.

#2-Get the doctor(s) who have more than 5 patients visited
cur.execute("SELECT Id, Name FROM doctor_details WHERE patients_visited >5 ")

result = cur.fetchall()

for x in result:
  print(x)

#Output:-
#(1, 'Chopper')
#(4, 'Kakashi')

#3-Get the doctors with no patients visit 
cur.execute("SELECT Id, Name FROM doctor_details WHERE patients_visited =0 ")
result = cur.fetchall()
for x in result:
  print(x)
  
#Output:-
#(2, 'Genos')







