"""
Programa que permita sacarle el porcentaje a un numero

"""

numero=int(input("Ingrese un numero: "))
porcentaje=int(input(f"Ingrese el porcentaje que desea saber del {numero}: "))

resultado=numero*porcentaje/100

print(f"el {porcentaje}% de {numero} es : {resultado}")