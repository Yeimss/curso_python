## 1. definir una clase (coche)

class Coche:
    # 2. Atributos o propiedades
    color = "Rojo"
    marca = "lamborgini"
    modelo= "2022"
    velocidad=300
    placa="VQO328"

    #3. Metodos (acciones de la clase)

    def acelerar(self):
        self.velocidadMax +=1
    
    def frenar(self):
        self.velocidad-=1
    
    def setColor(self, color):
        self.color=color
    
    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca=marca
    
    def getMarca(self):
        return self.marca

    def getVelocidad(self):
        return self.velocidad
    

#fin definición clase

#crear obj / instanciar la clase
print("-----------------COCHE 1------------------")

coche=Coche()

print(f"La velocidad actual es: {coche.getVelocidad()}")
print(f"El color del {coche.getMarca()} es: {coche.getColor()}")

for i in range (0,50):
    coche.frenar()

""" 
Esta parte comentaeda era para utilizar los setters y getters de la clase


newMarca=input("Ingrese una nueva marca para el coche: ")
newColor=input("Ingrese un nuevo color para el coche: ")
coche.setColor(newColor)
coche.setMarca(newMarca)

print(f"La velocidad actual es: {coche.getVelocidad()}")
print(f"El color del coche {coche.getMarca()} es: {coche.getColor()}")
"""

##Crear un nuevo objeto de la misma clase
print("-----------------COCHE 2------------------")
coche2=Coche()
coche2.setColor("Magenta")
coche2.setMarca("BMW")
print(f"La velocidad actual es: {coche2.getVelocidad()}")
print(f"El color del {coche2.getMarca()} es: {coche2.getColor()}")

for i in range (0,150):
    coche.frenar()

print(f"La velocidad actual es: {coche2.getVelocidad()}")

