import mysql.connector


mydb = mysql.connector.connect(
        host="localhost",
        user="liecharhall",
        passwd="E8a13244"
)
print( mydb )
