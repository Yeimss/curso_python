import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"OK, {usuario[1]}, vamos a crear una nueva nota")
        titulo=input("ingresa el titulo de tu nota: ")
        descripcion=input("ingresa la descripcion de tu nota: ")
        nota= modelo.Nota(usuario[0],titulo,descripcion)
        guardar=nota.guardar()

        if(guardar[0]>=1):
            print(f"Perfecto, has guardado la nota {nota.titulo}")

        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"{usuario[1]}, estas son tus notas: \n")
        nota=modelo.Nota(usuario[0],)
        notas=nota.mostrar()

        for nota in notas:

            print("------------------------------------")
            print(f"Titulo: {nota[2]}")
            print(f"Descripcion: {nota[3]}\n")

    def borrar(self, usuario):
        print(f"{usuario[1]} vamos a borrar una nota")
        titulo=input("Ingrese el titulo de la nota que desea borrar: ")
        nota=modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar() 
        if eliminar[0]>=1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado la nota, prueba nuevamente")