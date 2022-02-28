def holamundo(nombre):
    return f"Hola, qué tal {nombre}"

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