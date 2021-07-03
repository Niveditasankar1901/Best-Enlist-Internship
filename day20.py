import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword",
  database = "best-enlist"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE employee (Employee_id INTEGER PRIMARY KEY, Name VARCHAR(255), Salary FLOAT)")
#sql = "INSERT INTO employee (Employee_id, Name, Salary) VALUES (%s, %s, %s)"
#val = [
    #("101", "Gol D Roger", "50000"),
    #("102", "Shanks", "25000"),
    #("103", "Monkey D Luffy", "15000"),
    #("104", "Ronova Zoro", "10000"),
    #("105", "Bon Clay", "8000")
    #]
#mycursor.executemany(sql, val)
#mydb.commit()

#a. Write a query to get the maximum and minimum salary from employees table
mycursor.execute( "SELECT Name,Salary FROM  employee where Salary = (select max(Salary) from employee)" )
print(mycursor.fetchone())

#Output:-
#('Gol D Roger', 50000.0)

mycursor.execute( "SELECT Name,Salary FROM  employee where Salary = (select min(Salary) from employee)" )
print(mycursor.fetchone())
#Output:-
#('Bon Clay', 8000.0)

#b. Write a query to get the number of employees working with the company
mycursor.execute( "SELECT count(*) FROM  employee " )
print(mycursor.fetchone())
#Output:-
#(5,)

#c. Write a query to get the first 3 characters of first name from employees table
mycursor.execute( "SELECT SUBSTRING(Name,1,3) FROM employee" )
result = mycursor.fetchall()

for x in result:
  print(x)

#Output:-
#('Gol',)
#('Sha',)
#('Mon',)
#('Ron',)
#('Bon',)
