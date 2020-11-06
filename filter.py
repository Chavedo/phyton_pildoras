"""def numero_par(num):
    if num % 2==0:
        return True

numeros=[17,34,23,53,22,67,2,567,7]

print(list(filter(lambda numero_par: numero_par%2==0,numeros)))"""


class Empleado:
    def __init__(self, nombre, cargo, salario):

        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):

        return "{} que trabaja como {} tiene un salario de  {} $".format(
            self.nombre, self.cargo, self.salario
        )


listaEmpleados = [
    Empleado("Juan", "Director", 75444),
    Empleado("Ana", "Presidenta", 2333333),
    Empleado("Antony", "Administrativo", 299),
    Empleado("Pepe", "Asador", 234),
    Empleado("Mario", "Botnos", 21400),
]

salarios_altos = filter(lambda empleado: empleado.salario > 20000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)