from personaje import Personaje

class Enano(Personaje):

    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion="", clan=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__Clan=clan
    
    def __str__(self):
        return super().__str__()+'Clan: {}'.format(self.__Clan)

    def GetClan(self):
        return self.__Clan
    
    def SetClan(self, clan):
        self.__Clan=clan

    def Historia():
        return "Los elfos aparecen como seres prácticamente inmortales. Son los más hermosos, los más valientes y los de mayor sabiduría y poder."
    
    def Victoria(self):
        return "Nombre" + super().GetNombre() + "Ha ganado"
    
    def Derrota():
        return "Nombre" + super().GetNombre() + "Ha perdido"


    def AumentaVida(self, aumento):
        self.___vida= self.___vida + aumento




    def Atributos(self):
        super().Atributos()
        print("-Clan:", self.__Clan)
