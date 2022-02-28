"""
programa que reciba numeros y se salga cuando el usuario ingrese 111
"""
bandera=0
print("------------------ADIVINA EL NUMERO------------------")
while bandera==0:
    numero=int(input("Ingrese un numero: "))
    print(numero)
    if numero==111:
        bandera=2

print("-------FELICITACIONES!! ENCONTRASTE EL NUMERO-------")
