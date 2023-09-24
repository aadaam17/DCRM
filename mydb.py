# Install Mysql on computer
# http://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector or mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("DATABASE DONE!") 