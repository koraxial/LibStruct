print("Creating Database")
import mysql.connector
mydb = mysql.connector.connect(
     host ="localhost", 
     user ="########", 
     password ="########", 
     )
mycursor = mydb.cursor()
q1 = "create database Library"
mycursor.execute(q1)
print("Database created")

print("Creating Table")
mydb = mysql.connector.connect(
     host ="localhost", 
     user ="########", 
     password ="########", 
     database = "Library"
     )
mycursor = mydb.cursor()
q2 = "create table librarydb(SNo int, BookName varchar(100), AuthorName varchar(50), Price int, TotalQty int, Available int)"
mycursor.execute(q2)
print("Table created")
print("You can now use LibStruct")