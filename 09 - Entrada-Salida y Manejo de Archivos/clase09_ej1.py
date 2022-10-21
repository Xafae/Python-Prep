import sys

def clase09_ej1 (var1, var2, var3):
    if (sys.argv == 4):
        print ("El primer parametro es " + str(var1))
        print ("El segundo parametro es " + str(var2))
        print ("El tercer parametro es " + str(var3))
    else:
        print ("ERROR. Introdujo una cantidad incorrecta de parametros. Deben ser 3 en total")