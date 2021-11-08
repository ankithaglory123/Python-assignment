import mysql.connector



mydb = mysql.connector.connect(
host="rdsdemodb.cnsokhtjsei1.ap-southeast-1.rds.amazonaws.com",
user="admin",
password="admin123",
database="training"
)




mycursor = mydb.cursor()



#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Ganesh", "Banglore")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")



mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
print(myresult)
print("Name | Address")
for x in myresult:
print(x[0] +" | " + x[1])
print(type(x))
mydb.close()

pip install mysql.connector by Ganesh Babu M.
Ganesh Babu M.12:36 PM
pip install mysql.connector

