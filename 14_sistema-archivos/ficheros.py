from io import open
import pathlib

#Abrir archivo
ruta=str(pathlib.Path().absolute())+ "/14_sistema-archivos/texto.txt"
print(f"Aquí viene la ruta: {ruta}")


archivo=open(ruta, "a+")

#escribir en el archivo
#archivo.write('-------------soy un texto metido desde python-------------\n\n')

#cerrar el archivo
archivo.close()

#abrir el archivo con un permiso diferente
archivo_lectura=open(ruta, "r")

#leer contenido del archivo
""" contenido=archivo_lectura.read()
print(contenido) """

#leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:
    lista_frase=frase.split()
    #el split hace que cada separación por un espacio lo convierta en un elemento de una lista
    print(lista_frase)
