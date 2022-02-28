"""
Scrip con 4 variables:
lista
string
entero
bool

luego mostrar el dato y el tipo de variable
"""
lista=["perritos", "conejos", "caballos"]
titulo="A mirar el sp"
numero=4
mentira=False

variables=[lista,titulo,numero,mentira]

def variable_tipo (var):
    if isinstance(var, list):
        for i in var:
            print(f"{i}\n")
        print(f"la variable es: {type(var)}")
    else:
        print(f"la variable es: {var} \ny es de tipo: {type(var)}")



for x in variables:
    variable_tipo(x)
    print("\n\n")

