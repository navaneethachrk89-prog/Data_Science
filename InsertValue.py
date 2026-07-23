import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password='1989', database='python')

mycursur = conn.cursor()

sql = "insert into students (name,branch,id) values (%s,%s,%s)"
#value = ("shiva","cse",1)
#if multiple values are to be inserted then use executemany() method
values = [("shiva","cse",1),("sai","ece",2),("kumar","mech",3)]
mycursur.executemany(sql,values)
conn.commit()   
print(mycursur.rowcount,"record inserted")
      
    
    
    

