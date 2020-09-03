import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="liecharhall",
        passwd="E8a13244",
        database="sakila"
        )
mycursor = mydb.cursor()
mycursor.execute("SELECT last_name FROM actor")
myresult = mycursor.fetchone()
for row in myresult:
    print( row )
