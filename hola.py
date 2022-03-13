#PRIMERO DECLARO LOS TEXTOS A USAR EN ELMENÚ
menu_principal = ("""                                                                                                                                                                                                      
               B&&&! 7&&&&&&&&&&^                ==============================================================  
         .&&?7?7G&G7777777777B&&&Y               ||                                                          ||
       :@&77~^B@57!^^~~^^~~^^!77!5&G             ||                                                          ||
       ^@@~^^^!7~^^^111^~111^^^^^~!Y@#           ||                !Bienvenido a la pizzeria!                ||
       :@@~^^^^^^^^^111^!111^^^^^^^?@&.          ||                                                          || 
       :@@~^^^^^~~~^111^~111~~~~^^^~!?&&.        ||                                                          || 
       :@@~^^^^^7JJJ?!!~!!!?JJJ!^^^^^~!7&@:      ============================================================== 
       :@&!~~^^^~~~~~^7@@~^~~~~~^^^^^^^~@@^       
         :@@!^^^^^^^^^7@@!^^^^^^^~!!!!!!&@:      =====================  MENU PRINCIPAL ========================
         .@@!^^^^^^^^^~!!~^^^^^~~5@@@@@&^.        
         .&@?!~^^^^^^^^^^^^^^~~G@#Y55555&@:       1. Agregar Orden
           .&@Y!~^^^^^^^^^^^^#@#YYJJJJJY@@^       2. Despachar Orden
          ..&@@@5!!!!^^^^^^!!#@BJYYYJY5P&@:       3. Ver Ordenes actuales
        .:&&5YYY#@@@B!!77!7&@B5YJJJY5P&&.         4. Acerca del desarrollador
       :&&GP5555PPPPB@@&&&&&@@@#555G&#.           0. Salir 
         .&&&&&&&&&&&@B      P@&&&&G            
         """)

orden_nombre0= ("""
=================================================================================
!!                                                                             !!
!!                          Ingresa tu orden                                   !!
!!                                                                             !!
=================================================================================

        Por favor ingresa el nombre del cliente:   
""")

orden_direccion0= ("""
=================================================================================
!!                                                                             !!
!!                          Ingresa tu orden                                   !!
!!                                                                             !!
=================================================================================

        Por favor ingresa la direccion del cliente:   
""")

orden_pizzas0= ("""
=================================================================================
!!                                                                             !!
!!                          Ingresa una pizza                                  !!
!!                                                                             !!
=================================================================================

        Para continuar,elige tus ingredientes   
""")

orden_pizzas_mas = ("""
=================================================================================
!!                                                                             !!
!!                          Ingresa una pizza                                  !!
!!                                                                             !!
=================================================================================

        Deseas agregar otra pizza.............?  
        ("s" para Si, cualquier otra tecla para No):  
""")
orden_pizzas_tot = ("""
=================================================================================
!!                                                                             !!
!!                          Ingresa una pizza                                  !!
!!                                                                             !!
=================================================================================

        Todo listo, el precio de esta pizza es de :  
        """)

pepperoni = """
        Deseas agregarle Pepperoni....? ----------- Tiempo = 3 min 
        ("s" para Si, cualquier otra tecla para No):  
"""
salchicha = """
        Deseas agregarle Salchicha....? ----------- Tiempo = 3 min 
        ("s" para Si, cualquier otra tecla para No):   
"""
carne = """
        Deseas agregarle Carne....? ----------- Tiempo = 3 min 
        ("s" para Si, cualquier otra tecla para No):  
"""
queso = """
        Deseas agregarle Queso....? ----------- Tiempo = 3 min 
        ("s" para Si, cualquier otra tecla para No):  
"""
piña = """
        Deseas agregarle Piña....? ----------- Tiempo = 3 min 
        ("s" para Si, cualquier otra tecla para No):   
"""
otra_orden = """
        Deseas ordenar otra Pizza....? ----------- 
        ("s" para Si, cualquier otra tecla para No):  
"""

#PARTE FUNCIONAL 
from Lista_ordenes import ordenes_list,ingredientes_list,pizza_list

class Main:
    ordenes = ordenes_list()
    i = 0
    #METODOS A UTILIZAR
    def __init__(self) :
        self.main()
    def main(self):
        M = input(menu_principal+ "                                        "+"Ingrese una opcion valida para continuar: ")
        if M =='1':
            print ("1")
            self.ingresar_orden(self.ordenes)
        elif M =='2':
            print("Usted ha impreso 2")
        elif M =='3':
            self.ordenes.graficar_primero()
        elif M =='4':
            print("Usted ha impreso 4")
        elif M =='0':
            print("Adios")
            exit()
        else:        
            print("                            "+"Por favor, seleccione una opcion valida para continuar")
            self.main() #Vuelve a eecutar el codigo si no hay nada

    def ingresar_orden(self, ordenes0): #CREAR NUEVA ORDEN, no se si hacerlo con ordenes0 o solo self.ordenes pero no quiero arriesgarme
        pizzas = pizza_list()
        nombre_cliente = input(orden_nombre0)
        direccion_cliente = input(orden_direccion0)
        print(orden_pizzas0)
        self.ingresar_pizzas(pizzas) #INGRESA UN LISTADO DE PIZZAS
        self.i +=1
        ordenes0.añadir_primero ("Orden"+str(self.i),nombre_cliente,direccion_cliente,pizzas)
        print ("Orden agregada con exito")
        self.ordenes.recorrer()
        self.main()
        
        
    def ingresar_pizzas(self,pizzas0):#ARREGLO DE PIZZAS QUE SE MANDAN A LAS ORDENES
        lista_ing = self.agregar_ingredientes()
        pizzas0.añadir(lista_ing)
        listo = input(orden_pizzas_tot + str(pizzas0.ultimo.precio_total) + " Quetzales" +"\n        Y el tiempo total de preparacion sera de :\n        " + str(pizzas0.ultimo.tiempo_total) + " Minutos")
        mas = input(orden_pizzas_mas)
        if mas == "s":
            self.ingresar_pizzas(pizzas0)
        

    def agregar_ingredientes(self): # ARREGLO DE INGREDIENTES QUE SE MANDA A LAS PIZZAS
        ing =  ingredientes_list()
        pep = input(pepperoni)
        if pep == 's':
            ing.añadir ("Pepperoni",3,10)
        salch = input(salchicha)
        if salch == 's':
            ing.añadir ("Salchicha",4,10)
        car = input(carne)
        if car == 's':
            ing.añadir ("Carne",10,15)
        que = input(queso)
        if que == 's':
            ing.añadir ("Queso",5,35)
        piña0 = input(piña)
        if piña0 == 's':
            ing.añadir ("Piña",2,5)

        if ing.vacia() == True: #VALIDA QUE POR LO MENOS HAYA UN INGREDIENE
            print ("No puedes pedir una pizza sin ingredientes.......")
            la2 = self.agregar_ingredientes2(ing) #"CREO OTRO METODO IGUAL YA QUE SI NO SEBUGEA"
            while la2 == None:
                print("vacia")
                la2 = self.agregar_ingredientes2(ing) #"CREO OTRO METODO IGUAL YA QUE SI NO SEBUGEA"
            return (la2)
        else:
            print ("La pizza se ha ordenado con exito....")
            return (ing)

    def agregar_ingredientes2(self,ing): # ARREGLO DE INGREDIENTES QUE SE MANDA A LAS PIZZAS
        pep = input(pepperoni)
        if pep == 's':
            ing.añadir ("Pepperoni",3,10)
        salch = input(salchicha)
        if salch == 's':
            ing.añadir ("Salchicha",4,10)
        car = input(carne)
        if car == 's':
            ing.añadir ("Carne",10,15)
        que = input(queso)
        if que == 's':
            ing.añadir ("Queso",5,35)
        piña0 = input(piña)
        if piña0 == 's':
            ing.añadir ("Piña",2,5)
            ing.recorrer()
        while ing.vacia() == True: #VALIDA QUE POR LO MENOS HAYA UN INGREDIENE
            print ("No puedes pedir una pizza sin ingredientes......")
            self.agregar_ingredientes2(ing)
            
        return (ing)

new = Main()