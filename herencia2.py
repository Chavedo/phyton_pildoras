class Persona():
    def __init__(self,nombre,edad,lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar

    def descripcion(self):
        print("Nombre",self.nombre,",edad",self.edad,",reside en",self.lugar)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empl,edad_empl,lugar_empl):
        super().__init__(nombre_empl,edad_empl,lugar_empl)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario,"Antiguedad:",self.antiguedad)

antonio=Empleado(45555,20,"Antonio",55,"España")
antonio.descripcion()
print(isinstance(antonio,Empleado))
print(isinstance(antonio,Persona))
print(issubclass(Empleado,Persona))

