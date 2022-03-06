import mysql.connector

#conexion a la db
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="master_py",
)   
##print(database)
cursor=database.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS master_py')

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)