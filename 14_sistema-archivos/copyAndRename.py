from io import open
import pathlib, shutil

rutaOriginal=str(pathlib.Path().absolute())+ "/14_sistema-archivos/texto.txt"
rutaNueva=str(pathlib.Path().absolute())+ "/14_sistema-archivos/ficheroCopiado_NUEVO.txt"


""" 
##COPIAR
shutil.copyfile(rutaOriginal, rutaNueva)
"""


""" 
#RENAME
shutil.move(rutaOriginal, rutaNueva) 
"""


import os
""" 
#DELETE

os.remove(rutaNueva) 
"""

#comprobar si un fichero existe

import os.path
ruta=os.path.abspath("./")+"/14_sistema-archivos/texto.txt"
print(ruta)


if (os.path.isfile(ruta)):
    print("el archivo exixte")
else:
    print("el archivo no exixte")
