"""
mostrar todos los numeros pares del 1 al 100
"""

pares="{0"

for avanzar in range (2,101):
    if avanzar % 2 == 0:
        pares=pares+", "+str(avanzar)

print(f"Los numeros pares del 1 al 100 son: \nP={pares}")

for subidor in range (2,101):
    if subidor % 2 ==0:
        print(f"{subidor} es par")
    else:
        print(f"{subidor} es impar")