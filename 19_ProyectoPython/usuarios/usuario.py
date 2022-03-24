import datetime
import hashlib
from sqlite3 import connect
import usuarios.conexion as conexion

conectar=conexion.conectar()
database=conectar[0]
cursor=conectar[1]

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password

    def registrar(self):
        fecha=datetime.datetime.now()

        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql="INSERT INTO usuarios Values(null,%s,%s,%s,%s,%s)"
        user=(self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql,user)
            database.commit()
            result=[cursor.rowcount, self]
        except:
            result=[0, self]
        
        return result

    def identificar(self):
        #consulta para user+password
        sql="SELECT * FROM usuarios WHERE email=%s AND contraseña=%s"
        
        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario=(self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result=cursor.fetchone()

        return result