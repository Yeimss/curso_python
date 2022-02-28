"""
Hacer un programa que muestre todos los impares que diga el user
"""

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero mayor al anterior: "))
bandera=0

while bandera==0:
    if numero1>=numero2:
        numero2=int(input("Por favor ingrese un numero que sea mayor al primer numero: "))
    else:
        bandera+=1

print("\nLos numeros inpares entre estos dos numeros son: ")
for avanzar in range(numero1,numero2):
    if avanzar % 2 != 0:
        print(avanzar)
