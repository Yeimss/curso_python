##capturar excepxiones y manejar errores
#en casos suceptibles a fallos
try:
    nombre=input("Ingrese el nombre: ")

    if(len(nombre)>1):
        nombreUser="El nombre es: "+nombre

    print(nombreUser)
except:
    print("ha ocurrido un error, ingresa un nombre valido")
else:
    print("todo ha salido bien")
finally:
    print("lo que hay dentro del finally siempre se muestra, así haya error o no")

