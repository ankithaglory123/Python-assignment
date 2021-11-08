import mysql.connector
db = mysql.connector.connect(host="localhost", user="", password="Ankitha@3", database="task")
curzor = db.cursor()
y=curzor.execute("select * from task")
x=curzor.fetchall()
for i in x:
    print(i)