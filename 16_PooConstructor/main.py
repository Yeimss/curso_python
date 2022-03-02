from coche import Coche

carro=Coche("Amarillo", "Renault", "Clio", 100, "PDR130")
carro1=Coche("verde", "Mercedes", "ClaseA", 100, "KFL390")
carro2=Coche("azul", "BMW", "Z4", 100, "OMG301")
carro3=Coche("negro", "Audi", "Q10", 100, "WTF100")


print(carro.getInfo())

print(carro1.getInfo())

print(carro2.getInfo())

print(carro3.getInfo())


##detectar el tipo de dato de un obj

#print(type(carro3))

if(type(carro3)==Coche):
    print("Es un objeto correcto!!!")
else:
    print("no es un objeto")

#para imprimir una propiedad privada tiene que ser con un getter
print(carro.getPrivado())