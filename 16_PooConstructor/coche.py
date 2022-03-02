##definr la clase
class Coche:
    # 2. Atributos o propiedades
    color = "Rojo"
    marca = "lamborgini"
    modelo= "2022"
    velocidad=300
    placa="VQO328"


    #encapsulacion
    soyPublico="publico"
    __soyPrivado="Holi, soy privadiño"


    ##aquí viene el constructor
    def __init__(self, color, marca, modelo, velocidad, placa):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.placa=placa
        


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

    def setModelo(self,model):
        self.modelo=model

    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad=velocidad

    def getVelocidad(self):
        return self.velocidad
    
    def setPlaca(self, placa):
        self.placa=placa
    
    def getPlaca(self):
        return self.placa
    
    def getPrivado(self):
        return self.__soyPrivado

    def getInfo(self):
        info="\n\n-----Información del coche-------"
        info+="\n\tColor: "+self.getColor()
        info+="\n\tMarca: "+self.getMarca()
        info+="\n\tModelo: "+self.getModelo()
        info+=f"\n\tVelocidad: {self.getVelocidad()}"
        info+="\n\tPlaca: "+self.getPlaca()
        return info

#fin definición clase