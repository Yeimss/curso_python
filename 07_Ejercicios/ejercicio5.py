"""
programa que muestre todos los numeros que hay entre 2 numeros
"""

n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un numero mayor al anterior: "))
if n1>=n2:
    n2=int(input("por favor ingrese un numero mayor al primer numero: "))

for avanzar in range(n1+1,n2):
    print(avanzar)
else:
    print(F"ESOS SON TODOS LOS NUMEROS QUE HAY ENTRE {n1} y {n2}")
