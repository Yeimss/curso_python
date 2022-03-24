"""
proyecto python mySql:
-Abrir asistente
-login
-signIn
Cuando loguea puede hacer lo siguiente:
    crear nota
    mostrar notas
    borrar nota
"""
from usuarios import acciones
print(
"""
Acciones disponibles
    -Registro
    -Login
    -salir
"""
)
i=True
while i:
    accion=input("Qué quieres hacer?: ")
    doIt=acciones.Acciones()

    if(accion.upper()=="REGISTRO"):
        doIt.registro()
        i=False

    elif accion.upper()=="LOGIN":
        doIt.login()
        i=False

    elif accion.upper()=="SALIR":
        exit()
    
    else:
        print("ingrese una opcion valida\n\n")



