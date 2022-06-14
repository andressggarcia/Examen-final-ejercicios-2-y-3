#Examen de certificacion Emilio Garcia Giaquinta
#Ejercicio 3 JSON
import json
heroes= {
"nombre": "Flash",
"identidadSecreta": "Bartholomew Henry 'Barry' Allen",
"poderes": [
"Inmensa velocidad",
"agilidad",
"Electrokinesis"]},{"nombre": "Batman",
"identidadSecreta": "Bruce Wayne",
"poderes": ["Super fuerza",
"super velocidad"]},{"nombre": "Super Man",
"identidadSecreta": "Clark Joseph Kent","poderes": ["Super fuerza",
"super velocidad",
"resistencia",
"agilidad",
"reflejos",
"durabilidad",
"sentidos y longevidad"
]}
print(heroes)

with open("super_heroes.json", "w") as f:
    json.dump(heroes, f, indent=4)




#Ejercicio 2: POO
from operator import getitem
from operator import setitem
from os import remove


class Bicicleteria():
    def __init__(self, bicicletas, ganancias=0, cantidad_de_ventas=0):
        self.bicicletas = bicicletas
        self.ganancias = ganancias
        self.cantidad_de_ventas = cantidad_de_ventas

    def vender_bicicleta(self, bicicletas, ganancias, cantidad_de_ventas):
        self.cantidad_de_ventas += cantidad_de_ventas
        self.ganancias += ganancias
        self.bicicletas -= cantidad_de_ventas
        print("se vendieron",self.cantidad_de_ventas, " bicicletas")
        print("la ganancia es de:",self.ganancias, "pesos")
        print("las bicicletas que quedan son:",self.bicicletas)

    def comprar_bicicleta(self, bicicletas, ganancias):
        self.bicicletas += bicicletas
        self.ganancias -= ganancias
        print("se compraron:",self.bicicletas)
        print("quedan de ganancias:", self.ganancias, " pesos")




class Bicicleta():
    def __init__(self, nro_de_serie, modelo, año, precio):
        self.nro_de_serie = nro_de_serie
        self.modelo = modelo
        self.año = año
        self.precio = precio


    def __getitem__(self, nro_de_serie ):
        self.nro_de_serie = nro_de_serie

    def __setitem__(self, precio):
        self.precio = precio
    
    def __getitem__(self):
        return"El precio es de",{}," pesos"

    def __str__(self):
        return "el numero de serie es:{} modelo:{} año: {} precio:{}".format (self.nro_de_serie, self.modelo, self.año, self.precio)

Bicicleteria1 = Bicicleteria(5, 0, 0)
Bicicleteria1.vender_bicicleta(4, 120000, 4)
Bicicleteria1.comprar_bicicleta (1, 4000)

Bicicleta1 = Bicicleta({123890},{'vairo'},{2019},{120000})
print(Bicicleta1)