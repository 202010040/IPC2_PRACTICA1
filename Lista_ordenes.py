from clases import ingrediente_t,pizza_t,orden_t
from datetime import datetime, timedelta
import graphviz
import pydot

class ingredientes_list:

    
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False

    def unir (self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def añadir (self,nombre,tiempo,costo):
        new = ingrediente_t(nombre,tiempo,costo)
        if self.vacia():
            self.primero = self.ultimo = new
        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = new
            self.ultimo.anterior = temp
    
    def recorrer(self):
        if self.vacia():
            print("Está vacia")
        else:
            temp = self.primero
            while temp:
                print(temp.nombre) #Bucle a ejecutar
                temp = temp.siguiente
                if temp == self.primero:
                    break

########### ESTA CLASE NO TIENE METODOS APARTE DE LOS PROPIOS DE LA LISTAS CIRCULARES DOBLEMENTE ENLAZADAS #################

class pizza_list:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False

    def unir (self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def añadir (self,ingredientes):
        new = pizza_t(ingredientes)

        if self.vacia():
            self.primero = self.ultimo = new
        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = new
            self.ultimo.anterior = temp
    
    def recorrer(self):
        if self.vacia() ==True:
            print("Está vacia")
        else:
            temp = self.primero
            while temp:
                print("Los ingredientes que se van a usar en esta pizza son los siguientes:")#Bucle que se ejecuta por cada pizza
                temp0 = temp.ingredientes.primero
                while temp0:
                    print(temp0.nombre) #Bucle a ejecutar por cada ingrediente
                    temp0 = temp0.siguiente
                    if temp0 == temp.ingredientes.primero:
                        break
                print("El precio total de esta pizza será de: " + str(temp.precio_total)) 
                print("El tiempo total de esta pizza será de: " + str(temp.tiempo_total))    
                temp = temp.siguiente
                if temp == self.primero:
                    break

class ordenes_list:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False

    def unir (self):
        if self.vacia() == False:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def añadir_primero (self,numero,nombre,direccion,pizzas):
        new = orden_t(numero,nombre,direccion,pizzas)
        if self.vacia ():
            self.primero = self.ultimo = new
        else:
            temp = new
            temp.siguiente = self.primero
            self.primero.anterior = temp
            self.primero = temp
            self.unir()

    def añadir_ultimo(self,numero,nombre,direccion,pizzas):
        new = orden_t(numero,nombre,direccion,pizzas)
        if self.vacia ():
            self.primero = self.ultimo = new
        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = new
            self.ultimo.anterior = temp
            self.unir()
        

    def recorrer(self):
        if self.vacia():
            print("Está vacia")
        else:
            temp = self.primero
            while temp:
                print(temp.nombre,temp.precio_orden,temp.tiempo_orden) #Bucle a ejecutar
                temp.pizzas.recorrer()
                temp = temp.siguiente
                if temp == self.primero:
                    break
    
#################### AQUI COMIENZAN LOS METODOS A USAR #####################

    def sumar_tiempo(self):
        if self.vacia():
            print("Está vacia")
        else:
            temp = self.primero
            future = temp.hora + timedelta( minutes =120 )
            print(temp.nombre, temp.hora0, str(future.hour)+":"+str(future.minute))
            temp = temp.siguiente
            while temp != self.primero:
                future = temp.hora + timedelta( minutes =120 )
                print(temp.nombre, temp.hora0, str(future.hour)+":"+str(future.minute))
                temp = temp.siguiente
