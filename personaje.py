class Personaje():

#Constructor

    def __init__(self, nombre ="", raza ="", arma ="", vida =0, daño =0, bonificacion =""): 
        self.___nombre=nombre
        self.___raza=raza
        self.___arma=arma
        self.___vida=vida
        self.___daño=daño
        self.___bonificacion=bonificacion

#Método str

    def __str__(self):
        return "Nombre: {} - Raza: {} - Arma: {} - Vida: {} - Daño: {} - Bonificacion: {} ".format(self.___nombre, self.___raza, self.___arma, self.___vida, self.___daño, self.___bonificacion)


    def GetNombre(self):
        return self.___nombre
    
    def GetRaza(self):
        return self.___raza
    
    def GetArma(self):
        return self.___arma
    
    def GetVida(self):
        return self.___vida
    
    def GetDaño(self):
        return self.___daño

    def GetBonificacion(self):
        return self.___bonificacion


    def SetNombre(self,nombre):
        self.___nombre=nombre
    
    def SetRaza(self,raza):
        self.___raza=raza

    def SetArma(self,arma):
        self.___arma=arma

    def SetVida(self,vida):
        self.___vida=vida

    def SetDaño(self,daño):
        self.___daño=daño

    def SetBonificacion(self,bonificacion):
        self.___bonificacion=bonificacion
        
#Métodos extras
   
    def Combate():
        pass
    
    def Historia():
        pass
    
    def Victoria(self):
        pass
    
    def Derrota():
        pass
    
    def MensajeInicial():
        pass


    def Atributos(self):
        print("-Nombre:", self.___nombre)
        print("-Raza: ", self.___raza)
        print("-Arma: ", self.___arma)
        print("-Vida: ", self.___vida)
        print("-Daño: ", self.___daño)
        print("-Bonificacion:", self.___bonificacion)
