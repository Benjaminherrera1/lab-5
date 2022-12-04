from random import randint
from enano import Enano
from elfo import Elfo
from humano import Humano

lista_personaje=[]

enano=Enano("Magni","Enano", "Hacha", 100, 10, "Poder Interior", "Ullek" )
elfo=Elfo("Idril", "Elfo", "Espada", 100, 15, "Sudor Relampago" ,"Lindon")
humano=Humano("Björn", "Humano","Daga", 100, 5, "Modo Berserk", "Aesir" )
enano.Atributos()
elfo.Atributos()
humano.Atributos()
lista_personaje.append(enano)
lista_personaje.append(elfo)
lista_personaje.append(humano)


obj1=randint(0,2)
obj2=randint(0,2)
while obj1 == obj2:
    obj2 = randint(0,2)
turno = 1
while turno <= 10:
    if turno == 1:
        print(lista_personaje[obj1].GetVida())
        print(lista_personaje[obj2].GetVida())
    if lista_personaje[obj1].GetRaza() == "Humano":
        lista_personaje[obj1].SuperBono()
    print(lista_personaje[obj1].GetVida())
    print(lista_personaje[obj2].GetVida())
    if lista_personaje[obj1].GetRaza() == "Enano":
        aumento = int(input("Ingrese un numero entre 50 - 100: "))
        while aumento < 50 or aumento > 100:
            print("Numero al ingresado")
            aumento = int(input("Ingrese un numero entre 50 - 100: "))
        lista_personaje[obj1].Aumentavida(aumento)
    if lista_personaje[obj2].GetRaza() == "Elfo":
        lista_personaje[obj2].QuitaVida()
    if lista_personaje[obj2].GetRaza() == "Humano":
        lista_personaje[obj2].SuperBono()
    print(lista_personaje[obj1].GetVida())
    print(lista_personaje[obj2].GetVida())













