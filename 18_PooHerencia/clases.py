#HERENCIA: es la posibilidad de compartir atributos y metodos entre clases
#y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    def setNombre(self, n):
        self.nombre=n

    def setApellido(self, a):
        self.apellido=a

    def setAltura(self, h):
        self.altura=h

    def setEdad(self, e):
        self.edad=e

    def hablar(self):
        print(f"{self.nombre} está hablando")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

    def comer(self):
        print(f"{self.nombre} está comiendo")
    


class Informatico(Persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes="HTML, CSS, JS, PHP"
        self.experiencia=5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguaje):
        self.lenguajes=lenguaje
        return self.lenguajes
    
    def programar(self):
        return "estoy programando"
    
class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() #sirve para usar el constructor de la clase padre, osea de la clase de la que hereda
        self.auditarRedes="Experto"
        self.experienciaRedes=15

    def auditoria(self):
        return "estoy auditando una red"
    
    def getExperienciaRedes(self):
        return self.experienciaRedes
        
