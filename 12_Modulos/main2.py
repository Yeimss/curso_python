##Modulo de Matematicas

import math

numero=int(input("Ingrese el número al que le quiere sacar la raiz cuadrada: "))

def raiz(n):
    r=math.sqrt(n)
    return r

r=raiz(numero)
print(f"La raíz cuadrada de {numero} es: {r}")


print(f"Numero pi: {math.pi}")

print(f"Redondear arriba: {math.ceil(r)}")

print(f"Redondear abajo: {math.floor(r)}")



###Numeros random

import random

print(f"Numero aleatorio entre 15 y 67: {random.randint(15,67)}")


