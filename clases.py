from datetime import datetime
import time
class ingrediente_t:
    def __init__(self,nombre,tiempo,costo):
        self.nombre = nombre
        self.tiempo = tiempo
        self.costo = costo
        self.siguiente = None
        self.anterior = None
class pizza_t:
    def __init__ (self, ingredientes):
        self.ingredientes = ingredientes
        self.hora = datetime.now()
        self.precio_total = 0
        self.tiempo_total = 0
        self.siguiente = None
        self.anterior = None
        self.calcular_total()
        self.calcular_tiempo()

    def calcular_total(self): # Calcular total recorriendo y sumando los precios de los ingredientes 
        if self.ingredientes.vacia() == True:
            self.precio_total = 0
        else:
            temp_pizza = self.ingredientes.primero
            while temp_pizza:
                self.precio_total += temp_pizza.costo
                temp_pizza = temp_pizza.siguiente
                if temp_pizza ==  self.ingredientes.primero:
                    break

    def calcular_tiempo(self): # Calcular total recorriendo y sumando los precios de los ingredientes 
        if self.ingredientes.vacia() == True:
            self.tiempo_total = 0
        else:
            temp_pizza = self.ingredientes.primero
            while temp_pizza:
                self.tiempo_total += temp_pizza.tiempo
                temp_pizza = temp_pizza.siguiente
                if temp_pizza ==  self.ingredientes.primero:
                    break
class orden_t:
    def __init__(self,numero,nombre,direccion,pizzas):
        self.hora = datetime.now()
        self.hora0 = str(self.hora.hour)+":"+str(self.hora.minute)
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion
        self.pizzas = pizzas
        self.precio_orden = 0
        self.tiempo_orden = 0
        self.siguiente =None
        self.anterior = None
        self.calcular_total()
        self.calcular_tiempo()

    def calcular_total(self): # Calcular total recorriendo y sumando los precios de los ingredientes 
        if self.pizzas.vacia():
            self.precio_orden = 0
        else:
            temp_pizza = self.pizzas.primero
            while temp_pizza:
                self.precio_orden += temp_pizza.precio_total
                temp_pizza = temp_pizza.siguiente
                if temp_pizza ==  self.pizzas.primero:
                    break

    def calcular_tiempo(self): # Calcular total recorriendo y sumando los precios de las pizzas
        if self.pizzas.vacia():
            self.tiempo_orden = 0
        else:
            temp_pizza = self.pizzas.primero
            while temp_pizza:
                self.tiempo_orden += temp_pizza.tiempo_total
                temp_pizza = temp_pizza.siguiente
                if temp_pizza ==  self.pizzas.primero:
                    break