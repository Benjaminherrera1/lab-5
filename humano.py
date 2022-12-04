from personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion="", familia=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__Familia=familia
    
    def __str__(self):
        return super().__str__()+ "Familia {}".format(self.__Familia)

    def GetFamilia(self):
        return self.__Familia
    
    def SetFamilia(self, familia):
        self.__Familia=familia
    
    def Historia():
        return "Los elfos aparecen como seres prácticamente inmortales. Son los más hermosos, los más valientes y los de mayor sabiduría y poder."
    
    def Victoria(self):
        return "Nombre" + super().GetNombre() + "Ha ganado"
    
    def Derrota():
        return "Nombre" + super().GetNombre() + "Ha perdido"
    
    def MensajeInicial():
        pass

    def SuperBono():
        pass
    
    
    def Atributos(self):
        super().Atributos()
        print("-Familia:", self.__Familia)


           


    


    