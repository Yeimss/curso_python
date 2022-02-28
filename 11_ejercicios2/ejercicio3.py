"""
Programa que identifique si una variable está vacía
y si así es, llenarla con texto en minusculas y mostrarlo
en mayusculas
"""

texto=input("Ingrese lo que quiera (puede estar en blanco): ")

if(len(texto.strip())<=0):
    ###mostrar texto
    texto="hola mi genteeeeeeee"
    print(texto.upper())

else:
    print(f"La variable tiene este contenido: {texto}")
