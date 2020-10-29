class Coche():

    def __init__(self):

        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4  #__ encapsulacion
        self.enMarcha=False

    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos

        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    
    def estado(self):
       print("El coche tiene",self.__ruedas,"ruedas",
       "\tAncho",self.anchoChasis,"\tLargo",self.largoChasis)

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----A continuacion creamos el segundo objeto-----")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()
