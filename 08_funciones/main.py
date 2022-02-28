"""
Una funcion es un conjunto de instrucciones agrupadas bajo un mismo nombre en concreto que
puede reutilizarse cuantas veces sea necesario

SINTAXIS:

def nombre_funcion (parametros):
    Instrucciones...

"""
print("------------ EJEMPLO 1 ------------")
def mostrarNombres():
    print("James")
    print("Pablo")
    print("Maria")
    print("Jose")
    print("Santi")
    print("Memo")

mostrarNombres()
print("\n\n------------ EJEMPLO 2 ------------")

def mostrarTuNombre(name, edad):
    if edad<18:
        print(f"Hola, {name}, no puedes entrar porque eres menor de edad")
    else:
        print(f"Hola, {name}, puedes entrar")


for i in range(0,3):
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    mostrarTuNombre(nombre, edad)

print("\n\n------------ EJEMPLO 3 ------------")

def tabla(numero):
    print(f"~~~~~~~~~ TABLA DEL {numero} ~~~~~~~~~")
    for i in range (1,11):
        print(f"{numero} * {i} = {numero*i}")

bandera=0
while bandera==0:
    respuesta=input("Desea saber alguna tabla nueva (1.si, 2.no): ")
    if respuesta=="1":
        numero=int(input("Ingrese el numero del que quiere saber su tabla: "))
        tabla(numero)
    elif respuesta=="2":
        bandera=5

print("\n\n------------ EJEMPLO 4 ------------")
#Parametros opcionales


def getEmpleado(nombre, cc = None):
    print("EMPLEADO:")
    print(f"Nombre: {nombre}")
    if cc != None: 
        print(f"CC: {cc}")

getEmpleado("james")


