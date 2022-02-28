"""
programa que muestre los cuadrados de los primeros 60 numeros naturales
"""

contador=0
while contador<61:
    print(f"{contador}^2= {pow(contador,2)}")
    contador+=1