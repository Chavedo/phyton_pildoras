class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamiento_vehiculo(miVehiculo)