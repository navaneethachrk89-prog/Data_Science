import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password='1989', database='python')

if conn.is_connected():
    print('connection established')
print(conn)
print(conn.is_connected())

mycursur = conn.cursor()
mycursur.execute("create table students (name varchar(50),branch varchar(10), id int)")
mycursur.execute("show tables")
for x in mycursur:
    print(x)       
    
    
    

