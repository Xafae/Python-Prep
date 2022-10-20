#Matematicas.py


class Matematicas:
    def __init__(self, lista) -> None:
        try:
            if (len(lista) > 0):
                for elemento in lista:
                    assert type(elemento) == int or type(elemento) == float, f"La lista solo debe estar compuesta por numeros enteros o decimales"
                self.lista = lista
        except:
            raise ValueError("La lista no puede estar vacia")

    def esPrimo(self):
        for elemento in self.lista:
            self.__esPrimo(elemento)

    def esPrimoLista(self):
        lista_catcher = []
        for elemento in self.lista:
            lista_catcher.append(self.__esPrimoLista(elemento))
        for indice, x in enumerate(lista_catcher):
            print (indice, x)

    def factorial (self):
        for elemento in self.lista:
            if (self.__factorial(elemento)!="Error"):
                print(self.__factorial(elemento))

    def valorModal(self, eleccion):
            print(self.__valorModal(self.lista, eleccion))

    def convertidorTemperatura(self, origen, destino):
        verificar = "C", "F", "K"
        # assert origen in verificar, f"Solo se necesita C, F o K como origen"
        # assert destino in verificar, f"Solo se necesita C, F o K como destino"
        try:
            if (origen in verificar or destino in verificar):
                for elemento in self.lista:
                    print (self.__convertidorTemperatura(elemento, origen, destino))
        except ValueError:
                print ("Solo se necesita C, F o K como origen")

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
        if (eleccion == "Mayor" or eleccion == "Menor"):
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
        else:
            raise ValueError("Debe ingresar ""Mayor"" o ""Menor""")
             
    def __esPrimo(self, num):
        isPrimo = False
        if (num > 1 and type(num)==int):
                for x in range(2, num):
                    if (num%x==0):
                        isPrimo =False
                        break
                    else:
                        isPrimo= True 

                if (isPrimo):
                    print(str(num) + " Es primo")
                else:
                    print(str(num) + " NO es primo")    
        else:
            print(str(num) + " No se puede verificar si es primo. Solo numeros enteros y positivos son permitidos")
    
    def __esPrimoLista(self, num):
        isPrimo = False
        if (num > 1 and type(num)==int):
                for x in range(2, num):
                    if (num%x==0):
                        isPrimo =False
                        break
                    else:
                        isPrimo= True 
                return isPrimo    
        else:
            print(str(num) + " No se puede verificar si es primo. Solo numeros enteros y positivos son permitidos")
