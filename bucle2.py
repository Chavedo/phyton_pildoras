'''contador=0
miEmail=input("Introduce tu email: ")

for i in miEmail:
	if(i=="@" or i=="."):
		contador=contador+1


if contador==2:
	print("Email correcto")
else:
	print("incorrecto")'''

for i in range(5,10,2): #el tercer numero es de cuanto en cuanto
	print(f"Valor de la variable {i}") #f concatena texto con variables