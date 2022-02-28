"""
Librerias ya hechas para utilizar y ayudarnos a que nuestro codigo se haga más easy

podemos encontrar modulos aqui:
https://docs.python.org/3/py-modindex.html

o podemos hacer nuestrso propios modulos
"""

## moduloPropio
##import miModulo

#print(miModulo.calculadora(8,2, True))
#print(miModulo.holamundo("Jamesito"))


## Modulo de FECHAS
import datetime

hoy=datetime.date.today()
fecha_completa=datetime.datetime.now()

print(fecha_completa.year)

fecha_personalizada=fecha_completa.strftime('%d/%m/%Y, %H:%M:%S')
print(f"Fecha personalizada: {fecha_personalizada}")