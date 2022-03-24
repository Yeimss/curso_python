import usuarios.usuario as modelo
import notas.acciones as notas

class Acciones:
    def registro(self):
        print("\nOK, identificate en el sistema")
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        email=input("Email: ")
        password=input("contraseña: ")

        usuario=modelo.Usuario(nombre, apellido, email, password)
        registro=usuario.registrar()

        if registro[0]>=1:
            print(f"perfecto {registro[1].nombre} te has registrado correctamente con el email: {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    
    def login(self):
        try:
            print("OK, vamos a ingresar en el sistema")
            email=input("Email: ")
            password=input("contraseña: ")

            usuario=modelo.Usuario('','',email,password)
            login=usuario.identificar()

            if email==login[3]:
                print(f"Bienvenido/a a notitas, {login[1]} -- fecha: {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto")
        
    def proximasAcciones(self, usuario):
        print(
            """
            
            Acciones disponibles:
            -Crear nota(crear)
            -Mostrar tus notas(mostrar)
            -Eliminar nota (eliminar)
            -salir
            """)
        accion=input("¿Qué quieres hacer?: ")
        hazEl=notas.Acciones()


        if accion.upper()=="CREAR":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion.upper()=="MOSTRAR":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion.upper()=="ELIMINAR":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion.upper()=="SALIR":
            print("goodbye")
            exit()
        
        else:
            print("OPCION INCORRECTA!!!")
            self.proximasAcciones(usuario)





