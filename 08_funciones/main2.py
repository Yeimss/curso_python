print("\n\n------------ EJEMPLO 5 ------------")

#Parametros opcionales + return
def saludame(nombre):
    saludo=f"Muy buenos días, {nombre}"
    return saludo

hola=saludame("David")
print(hola)

print("\n\n------------ EJEMPLO 6 ------------\n\n")

def calculadora (n1,n2,basicas=False):
    suma=n1+n2
    resta=n2-n2
    multiplicacion=n1*n2
    division=n1/n2

    cadena=""
    if basicas==True:
        cadena+=f"Suma= {suma}\n"
        cadena+=f"Resta= {resta}\n"
    else:
        cadena+=f"Multiplicacion= {multiplicacion}\n"
        cadena+=f"Division= {division}\n"
    return cadena

print(calculadora(16,2,True))

print("\n\n------------ EJEMPLO 7 ------------\n\n")

def name(nombre):
    texto=f"El nombre es: {nombre}\n"
    return texto

def apellido(apellido):
    texto=f"El apellido es: {apellido}"
    return texto

def getCompleteName(nombre, a):
    texto=f"{name(nombre)}{apellido(a)}"
    return texto

print(getCompleteName("jamesito","herrera"))
    

print("\n\n------------ EJEMPLO 8 ------------\n\n")

dimeElYear= lambda year: f"El año es {year}"

print (dimeElYear(2034))