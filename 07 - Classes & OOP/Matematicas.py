class Matematicas:
    def __init__(self, lista) -> None:
        self.lista = lista
        pass

    def esPrimo(self):
        for elemento in self.lista:
                if (self.__esPrimo(elemento)):
                    print(str(elemento) + " Es Primo")
                else:
                    print(str(elemento) + " NO es primo")

    def factorial (self):
        for elemento in self.lista:
            if (self.__factorial(elemento)!="Error"):
                print(self.__factorial(elemento))

    def valorModal(self, eleccion):
        if (eleccion=="Mayor"):
            print(self.__valorModal(self.lista, "Mayor"))
        else:
            print(self.__valorModal(self.lista, "Menor"))

    def convertidorTemperatura(self, origen, destino):
            for elemento in self.lista:
                    print (self.__convertidorTemperatura(elemento, origen, destino))

    def __factorial (self, numRecibido):
        factorial = 1
        if (numRecibido>0 and type(numRecibido)==int):
            while (numRecibido >0):
                factorial = factorial * numRecibido
                numRecibido -= 1
            return factorial
        else:
            print ("El numero debe ser un entero positivo")
            return "Error"
    
    def __convertidorTemperatura(self, value, origen, destino):
            if (origen =="C" and destino =="F"):
                return (value * 9/5) + 32
            elif (origen == "C" and destino == "K"):
                return value + 273.15
            elif (origen == "F" and destino == "C"):
                return (value - 32) * 5/9
            elif (origen == "F" and destino == "K"):
                return (value + 459.67) * 5/9
            elif (origen == "K" and destino == "F"):
                return 9/5*(value - 273.15) +32
            elif (origen == "K" and destino == "C"):
                return value - 273.15
            else:
                return value

    
    def __valorModal (self, lista, eleccion):
        contadorMenor = 0
        contadorMayor = 0
        finderMenor = ""
        finderMayor = ""
        for elemento in lista:
            if (lista.count(elemento) > contadorMayor):
                if (contadorMenor < contadorMayor):
                    contadorMenor = contadorMayor
                    finderMenor = finderMayor
                contadorMayor = lista.count(elemento)
                finderMayor = elemento
        if(eleccion == "Mayor"):
            return "El elemento es " + str(finderMayor) + " y se repite " + str(contadorMayor) + " veces"
        else:
            return "El elemento es " + str(finderMenor) + " y se repite " + str(contadorMenor) + " veces"

    def __esPrimo(self, num):
        isPrimo = False
        if (num > 1 and type(num)==int):
            for x in range(2, num):
                if (num%x==0):
                    isPrimo =False
                    break
                else:
                    isPrimo= True          
            return isPrimo
