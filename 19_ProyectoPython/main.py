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
"""
)
accion=input("Qué quieres hacer?: ")
doIt=acciones.Acciones()

if(accion.upper()=="REGISTRO"):
    doIt.registro()

elif accion.upper()=="LOGIN":
    doIt.login()

