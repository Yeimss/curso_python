from typing import Text


nombre="Jamesito"

##funciones generales
print(type(nombre))

#detectar el tipado
comprobar= isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string :3")
else:
    print("No es un string .-.")

if not isinstance(nombre, float):
    print("la variable no es un racional")


#limpiar espacios
frase="                mi contenido  "
print(frase)
print(frase.strip())

#eliminar variables
year=2022
print(year)
del year


#comprobar tamaño de la variable
texto="perejil"
print(f"La variable tiene {len(texto)} caracteres")

#encontrar caracteres
frase="la vida es bella"
print(frase.find("vida"))

#reemplazar palabras en un string
nueva_frase=frase.replace("vida", "moto")
print(nueva_frase)