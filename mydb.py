import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", passwd="Baphuoc1104#")

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRMapplication")

print("MySQL connected to application!")
