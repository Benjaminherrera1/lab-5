from personaje import Personaje

class Elfo(Personaje):

    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion="", reino=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__Reino=reino

    def __str__(self):
        return super().__str__()+ "Reino: {}".format(self.__Reino)

    def GetReino(self):
        return self.__Reino
    
    def SetReino(self, reino):
        self.__Reino=reino

    def Historia():
        return "Los elfos aparecen como seres prácticamente inmortales. Son los más hermosos, los más valientes y los de mayor sabiduría y poder."
    
    def Victoria(self):
        return "Nombre" + super().GetNombre() + "Ha ganado"
    
    def Derrota():
        return "Nombre" + super().GetNombre() + "Ha perdido"
        
    def QuitaVida(self):
        super().SetVida(super().GetVida() - int(super().GetVida() * 0,1))
        
    def Atributos(self):
        super().Atributos()
        print("-Reino:", self.__Reino)