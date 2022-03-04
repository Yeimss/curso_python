#para usar swlite primero hay que importar el modulo
import sqlite3

#conexion a la base de datos
conexion=sqlite3.connect('pruebas.db')

#crear curson
cursor= conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"descripcion TEXT,"+
"precio INT(255)"+
")")

#Guardar cambios
conexion.commit()

#ingresar datos en una tabla
""" 
cursor.execute("INSERT INTO productos VALUES(null,'borojo','rico borojo para que seas like a beast',1000)")
conexion.commit()
"""
#listar datos
cursor.execute("SELECT * FROM productos")
productos=cursor.fetchall()

for producto in productos:
    print("id: ", producto[0])
    print("titulo: ", producto[1])
    print("descripcion: ", producto[2])
    print("precio: ", producto[3],"\n\n")




#cerrar la conexión
conexion.close()
