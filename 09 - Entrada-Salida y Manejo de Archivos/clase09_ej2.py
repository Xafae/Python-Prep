import datetime

def Pronostico_climatico (grados, humedad, llovio):
    archivo = open(r"C:\Users\Admin\Desktop\Python-Prep\09 - Entrada-Salida y Manejo de Archivos\clase09_ej2.csv", "a")
    archivo.write(str(datetime.datetime.now()) +", " + str(grados) + ", "+ str(humedad) +", "+ str(llovio))
    archivo.close()

Pronostico_climatico (25, 38, False)