import mysql.connector

#conexion a la db
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database='master_py'
)   
##print(database)
cursor=database.cursor(buffered=True)

cursor.execute('CREATE DATABASE IF NOT EXISTS master_py')

""" cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
 """
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar (40) NOT NULL,
    modelo varchar (40) NOT NULL,
    precio float(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo primary key(id)
    )
    """
)


##insertar datos
""" 
cursor.execute("INSERT INTO vehiculos VALUES(NULL, 'opel', 'astra', 18500000)")
database.commit()
"""
""" 
coches=[
    ('chevrolet', 'aveo', 22000000),
    ('Mazda', 'Mazda3', 60000000),
    ('Audi', 'R8',12000000),
]

cursor.executemany("INSERT INTO vehiculos VALUES(NULL,%s ,%s ,%s )", coches)
database.commit()
 """



##actualizar
""" 
cursor.execute("UPDATE vehiculos set marca='seat', modelo='leon' where id=2;")
database.commit() 
"""

cursor.execute("SELECT * FROM vehiculos ORDER BY marca")
carriños=cursor.fetchall()

for carro in carriños:
    print(f"id: ",carro[0])
    print(f"marca: ",carro[1])
    print(f"modelo: ",carro[2])
    print(f"precio: ",carro[3])
