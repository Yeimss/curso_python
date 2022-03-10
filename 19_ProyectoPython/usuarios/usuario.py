import mysql.connector
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='master_py',
    port=3306

)

cursor=database.cursor(buffered=True)
print(database)

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password

    def registrar(self):
        sql="INSERT INTO usuarios Values(null,%s,%s,%s,%s,%s)"

    def identificar(self):
        return self.nombre