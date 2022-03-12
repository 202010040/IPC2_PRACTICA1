import xml.etree.ElementTree as ET
from temp import piso_t, patron_t
from Lista_clases import pisos_list,patron_list

z = input("Hola, por favor escribe la ruta del xml")
zz = open(str(z))
tree = ET.parse(zz)
root = tree.getroot()
piso_nombre = "" #GUARDAR EL NOMBRE DEL PISO
piso_rows = 0 #GUARDA LAS FILAS
piso_col = 0#GUARDA LAS COLUMNAS
piso_vol = 0#Costo de volteo
piso_in = 0 #Costo de intercambio

patron_codigo = ""
patron_texto = ""

Pisos = pisos_list()

for pisos in root.findall("piso"): #RECORRE TODOS LOS PISOS
    Patrones = patron_list ()
    piso_nombre = pisos.get("nombre")
    for filas in pisos.findall("R"):#OBTIENE LAS FILAS
        piso_rows = int (filas.text)
    for columnas in pisos.findall("C"):#OBTIENE LAS COLUMNAS
        piso_col = int (columnas.text)
    for volteos in pisos.findall("F"):#OBIENE EL COSTO DE VOLTEO
        piso_vol = int (volteos.text)
    for intercambios in pisos.findall("S"):#OBTIENE EL COSTO DE INTERCAMBIO
        piso_in = int (intercambios.text)
    for patrones in pisos.findall("patrones"): #POR CADA PISO BUSCA LOS PATRONES 
        for patron in patrones.findall("patron"): #BUSCA CADA PATRON PORQUE HAY UN NIVEL DE MÁS
         patron_codigo = str(patron.get("codigo")) #OBTIENE EL CODIGO DEL PATRON
         patron_texto = str (patron.text).strip() #OBTIENE EL MERO PATRON DE COLORES
         Patrones.añadir(patron_codigo,patron_texto)
    Pisos.añadir (piso_nombre,piso_rows,piso_col,piso_vol,piso_in,Patrones)

Pisos.mosaico1()
Pisos.file()