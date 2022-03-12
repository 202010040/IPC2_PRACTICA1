from Lista_ordenes import ordenes_list,ingredientes_list,pizza_list
ing =  ingredientes_list()
ing.añadir ("Queso",3,50)
ing.añadir ("Salami",5,70)
ing.añadir ("noruego",2,50)
ing.añadir ("Atun",5,90)

pizza = pizza_list()
pizza.añadir(ing)

orden1 = ordenes_list()
orden1.añadir_primero("3","El caballo Juan","El establo",pizza)
orden1.recorrer()

