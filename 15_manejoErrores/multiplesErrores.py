##manejo de multiples errores

""" 
try:
    numero=int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es:" +str(numero*numero))
except TypeError:
    print("debes convertir tus cadenas a entero: ")
#except ValueError:
#   print("Introduce un número correcto")
except Exception as e:
    print(f"Ha ocurrido un error de tipo: {type(e).__name__}")

"""

#excepciones personalizadas
try:
    nombre=input("Ingrese un nombre: ")
    edad=int(input("Ingrese la edad: "))

    if edad < 5 and edad >110:
        raise ValueError("La edad introducida no es real >.<")
    elif len(nombre)<=1:
        raise ValueError("El nombre no está completo .-.")

    print(f"Bienvenido {nombre}")
except ValueError:
    print("Introducí bien los datos hdp")


