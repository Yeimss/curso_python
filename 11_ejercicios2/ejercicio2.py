"""
Crear un programa que añada elemenetos a una lista siempre que la lista sea menor a cierto numero
"""

cantidad=int(input("Ingrese la cantidad de elementos que desea ingresar: "))
ciclo=int(input("¿Qué ciclo desea usar?: \n1.while.\n2.for.\n"))

lista=[]
if ciclo==1:
    contador=0
    while contador<cantidad:
        nuevoElemento=input("Ingrese un elemento porfis: ")
        lista.append(nuevoElemento)
        contador+=1

elif ciclo==2:
    for x in range (0,cantidad):
        nuevoElemento=input("Ingrese un elemento porfis: ")
        lista.append(nuevoElemento)

print(lista)