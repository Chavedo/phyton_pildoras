print("Asignaturas optativas")
print("Informatica grafica - Prueba de software - Usabilidad y accesibilidad")
opcion=input("Introduce la asignatura: ")
asignatura=opcion.lower()
#lower transforma todo en minusculas <--
#upper en mayusculas

if asignatura in ("informatica grafica","prueba de software","utilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura no corresponde")

#case sensitive
#in= verifica si esta dentro del in