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
            i = 0
            temp = self.primero
            while temp:
                print ("\n-------------------"+" Pizza #"+str(i)+ " ---------------------")
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

    def graficar_pizzas (self):
        text_pizza = ""
        
        temp = self.primero
        j = 0
        temp.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j)
        while temp:
            temp0 = temp.ingredientes.primero
            temp.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j)
            
            text_pizza += "\n " + temp.hora + "[label = \" pizza" + str(j) +  " " + r'\n' +" " + "Ingredientes que lleva: " +  " " + r'\n' +" "
            while temp0:
                text_pizza += str(temp0.nombre) +  " " + r'\n' +" "
                temp0 = temp0.siguiente
                if temp0 == temp.ingredientes.primero:
                    break
            text_pizza += ("El precio total de esta pizza será de: " + str(temp.precio_total)) + "\"" + "]"  + "\n" 
            if temp.siguiente != None:
                temp.siguiente.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j+1)
                text_pizza += "\n" + temp.hora+ "->" + temp.siguiente.hora + "\n"
            else:
                text_pizza += "\n" + temp.anterior.hora+ "->" + temp.hora + "\n"
            j += 1
            temp = temp.siguiente
            if temp == self.primero:
                break
        return (text_pizza)

    def graficar_pizzas_primero (self):
        text_pizza = ""
        
        temp = self.primero
        j = 0
        temp.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j)
        while temp:
            temp0 = temp.ingredientes.primero
            temp.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j)
            
            text_pizza += "\n " + temp.hora + "[label = \" pizza" + str(j) +  " " + r'\n' +" " + "Ingredientes que lleva: " +  " " + r'\n' +" "
            while temp0:
                text_pizza += str(temp0.nombre) +  " " + r'\n' +" "
                temp0 = temp0.siguiente
                if temp0 == temp.ingredientes.primero:
                    break
            text_pizza += ("El precio total de esta pizza será de: " + str(temp.precio_total)) + "\", color = \"darkgreen\", fontcolor = \"darkgreen\"" + "]"  + "\n" 
            if temp.siguiente != None:
                temp.siguiente.hora = str (datetime.now().strftime("%H:%M:%S")).replace(":","") + str(j+1)
                text_pizza += "\n" + temp.hora+ "->" + temp.siguiente.hora + "\n"
            else:
                text_pizza += "\n" + temp.anterior.hora+ "->" + temp.hora + "\n"
            j += 1
            temp = temp.siguiente
            if temp == self.primero:
                break
        return (text_pizza)

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
                print ("\n==================== "+ temp.numero + " ========================")#Bucle a ejecutar
                print ("Hora de la orden: "  + temp.hora0)
                print ("Nombre del cliente:  " + temp.nombre )
                print ("Direccion del cliente:  " + temp.direccion )
                print ("Tiempo total:  " + str(temp.tiempo_orden) )
                print ("Costo total:  " + str(temp.precio_orden) )
                print ("las pizzas ordenadas fueron las siguientes:")
                temp.pizzas.recorrer()
                temp = temp.siguiente
                if temp == self.primero:
                    break
    
#################### AQUI COMIENZAN LOS METODOS A USAR #####################

    def graficar_normal (self): #"crea un texto para usar como dot"

        text = """digraph G {
        node [shape=record]
        label="Listado de ordenes actuales: " labelloc=t \n"""

        temp = self.primero
        while temp:
                text += "subgraph " + str(temp.numero) + "{ \n"
                text += "label = " + str(temp.numero) + "\n"
                text += "struct" + str(temp.numero).replace("#","") + "[label = \"{" +"Hora de la orden: " + str(temp.hora0) + " | " + "Nombre del cliente: " +  str(temp.nombre) + " | " + "Direccion del cliente: " + str(temp.direccion) + " min"+ " | " +"Tiempo de la orden: " + str(temp.tiempo_orden) + " | "+ "Total a pagar : Q" + str(temp.precio_orden) + " }\" ] "
                text += temp.pizzas.graficar_pizzas()
                text += "\n }"
                temp = temp.siguiente
                if temp == self.primero:
                    break

        text += " \n }"
        print (text)

    def graficar_primero (self): #"crea un texto para usar como dot"

        text = """digraph G {
        node [shape=record]
        label="Listado de ordenes actuales: " labelloc=t \n"""

        temp = self.primero
        text += "subgraph " + str(temp.numero) + "{ \n"
        text += "label = " + str(temp.numero) + "\n"
        text += "\n" " fontcolor = \"darkgreen\" "
        text += "struct" + str(temp.numero).replace("#","") + "[label = \"{" +"Hora de la orden: " + str(temp.hora0) + " | " + "Nombre del cliente: " +  str(temp.nombre) + " | " + "Direccion del cliente: " + str(temp.direccion) + " min"+ " | " +"Tiempo de la orden: " + str(temp.tiempo_orden) + " | "+ "Total a pagar : Q" + str(temp.precio_orden) + " }\", color = \"darkgreen\", fontcolor = \"darkgreen\" ] "
        text += temp.pizzas.graficar_pizzas_primero()
        text += "\n" " style = \"filled\" "
        text += "\n" " color = \"springgreen\" "
        text += "\n }"
        temp = temp.siguiente
        while temp:
                text += "subgraph " + str(temp.numero) + "{ \n"
                text += "label = " + str(temp.numero) + "\n"
                text += "struct" + str(temp.numero).replace("#","") + "[label = \"{" +"Hora de la orden: " + str(temp.hora0) + " | " + "Nombre del cliente: " +  str(temp.nombre) + " | " + "Direccion del cliente: " + str(temp.direccion) + " min"+ " | " +"Tiempo de la orden: " + str(temp.tiempo_orden) + " | "+ "Total a pagar : Q" + str(temp.precio_orden) + " }\" ] "
                text += temp.pizzas.graficar_pizzas()
                text += "\n }"
                if temp == self.primero:
                    break
        text += " \n }"
        print (text)

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
