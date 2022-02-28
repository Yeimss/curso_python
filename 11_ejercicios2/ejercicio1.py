"""
Programa con una lista con 8 Numeros enteros
1. mostrarla
2. ordenarla
3. longitud
4. buscar un elemento
"""
def mostrar(lista):
        print(lista)

def buscar(lista, elemento):
    pertenece=elemento in lista
    if pertenece:
        print(f"El elemento está en la posición {lista.index(elemento)}")
    else:
        print("El elemento no pertenece a la lista.")


numeros=[4,5,12,3,1,20,18,13]
n=1
while n==1:
    opcion=int(input("\n\n¿Que desea hacer?: \n1. mostrar. \n2. ordenar.\n3.ver la longitud. \n4. Buscar un elemento.\n5. Salir.\n"))
    if opcion==1:
        mostrar(numeros)
    elif opcion==2:
        numeros.sort()
    elif opcion==3:
        print(f"La longitud de la lista es: {len(numeros)}")
    elif opcion==4:
        ele=int(input("Ingrese el numero que desea buscar: "))
        buscar(numeros, ele)
    elif opcion==5:
        n+=1

        



