import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password='1989')

if conn.is_connected():
    print('connection established')
print(conn)
print(conn.is_connected())

mycursur = conn.cursor()
mycursur.execute("show databases")
for db in mycursur:
    print(db)       
    
    

