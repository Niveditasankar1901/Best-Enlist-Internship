#Day 24
#1. Create a JSON of all object types and import the JSON into a SQL Database

import mysql.connector
import json

data=[
    {"Name" : "Levi", "Anime" : "Attack on Titan", "Role" : "Captain of the Survey Corps", "Age":"30","protagonist":False},
    {"Name" : "Luffy", "Anime" : "One piece", "Role" : "Captain of the pirate ship", "Age":"19","protagonist":True},
    {"Name" : "Saitama", "Anime" : "One punch man", "Role" : "B-class hero", "Age":"25","protagonist":True},
    {"Name" : "Zoro", "Anime" : "One piece", "Role" : "Swordman", "Age":"21","protagonist":False,}
    ]
x=json.dumps(data)


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Yourpassword",
  database = "best-enlist"
)

dbse=db.cursor()

dbse.execute("CREATE TABLE json_records(Name VARCHAR(255),Anime VARCHAR(255),Role VARCHAR(255), Age int, protagonist VARCHAR(255))")
sql="INSERT INTO json_records(Name, Anime, Role, Age,  protagonist ) VALUES (%s)"

for i in range(len(x)):
    json_records[i]=x[i]





