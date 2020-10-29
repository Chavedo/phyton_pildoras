print("Programa de evaluacion de alumnos")

nota_alumno=input("Intruduzca la nota: ")

def evaluacion(nota):
	if nota<=5 and nota>0:
		valoracion="suspenso"
	elif nota>6 and nota<=10:
		valoracion="aprobado"
	else:
		valoracion="no valido"
	return valoracion

print(evaluacion(int(nota_alumno)))
