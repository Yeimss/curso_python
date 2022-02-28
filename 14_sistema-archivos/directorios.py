import os
import shutil

#crear carpeta
""" 
if not os.path.isdir("./carpetita"):
    os.mkdir("./carpetita")
else: 
    print("Ya existe el directorio")
"""
""" 
#eliminar carpeta
os.rmdir("./carpetita")
"""

##copiar la carpeta
""" rutaCarpeta="./carpetita"
rutaNueva="./14_sistema-archivos/carpetita"
shutil.copytree(rutaCarpeta, rutaNueva) """

#contenido de la carpeta
print("---------Contenido de mi carpeta---------")

contenido=os.listdir("./14_sistema-archivos/carpetita")
print(contenido)

for fichero in contenido:
    print("fichero: "+fichero)