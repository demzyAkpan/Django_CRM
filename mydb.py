import mysql.connector
#install mysql on your computer
#pip install mysql-server
#pip install mysql-connector
#pip install mysql-connector-python
#pip install mysql or pymysql (which is a pure-python MySQL client)
#create a database connector
#git: https://github.com/flatplanet/Django-CRM  
database = mysql.connector.connect(

host = 'localhost',
user = 'root',
passwd = 'Is.not.password'

)

#prepare a cursor object
cursorobject = database.cursor()

#create database
cursorobject.execute("CREATE DATABASE almartco")

print("All done!")