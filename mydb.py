import mysql.connector

dataBase=mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='240695'
)

cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE vak")

print('All done')