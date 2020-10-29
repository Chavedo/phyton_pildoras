class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self):
        self.enMarcha=True
    def estado(self):
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
miCoche=Coche()

print("Largo coche:",miCoche.largoChasis)
print("Tiene",miCoche.ruedas,"ruedas")
miCoche.arrancar()
print(miCoche.estado())