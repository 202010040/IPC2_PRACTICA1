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
orden_pizzas_mas = ("""
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
    #METODOS A UTILIZAR
    def __init__(self) :
        self.main()
    def main(self):
        M = input(menu_principal+ "                                        "+"Ingrese una opcion valida para continuar: ")
        if M =='1':
            print ("1")
            self.ingresar_orden()
        elif M =='2':
            print("Usted ha impreso 2")
        elif M =='3':
            print("Usted ha impreso 3")
        elif M =='4':
            print("Usted ha impreso 4")
        elif M =='0':
            print("Usted ha impreso 0")
        else:        
            print("                            "+"Por favor, seleccione una opcion valida para continuar")
            self.main() #Vuelve a eecutar el codigo si no hay nada

    def ingresar_orden(self):
        nombre_cliente = input(orden_nombre0)
        direccion_cliente = input(orden_direccion0)
        print(orden_pizzas0)
        self.ingresar_pizzas()
        
    def ingresar_pizzas(self):#ARREGLO DE PIZZAS QUE SE MANDAN A LAS ORDENES
        pizzas = pizza_list()
        lista_ing = self.agregar_ingredientes()
        lista_ing.recorrer()

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
            print ("Por favor escoja por lo menos un ingrediente....")
            self.ingresar_pizzas()
        else:
            print ("La pizza se ha ordenado con exito....")
            ing.recorrer()
            return (ing)

new = Main()