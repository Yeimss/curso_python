from io import open
import pathlib

#Abrir archivo
ruta=str(pathlib.Path().absolute())+ "/14_sistema-archivos/texto.txt"
print(f"Aquí viene la ruta: {ruta}")


archivo=open(ruta, "a+")

#escribir en el archivo
archivo.write('-------------soy un texto metido desde python-------------\n\n')

#cerrar el archivo
archivo.close()
