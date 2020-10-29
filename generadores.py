'''def generaPares(limite):
	num=1
	while num<limite:
		yield num*2
		num=num+1
devuelvePares=generaPares(10)

print(next(devuelvePares))

print("asdcasd")

print(next(devuelvePares))

print("asdcasd")'''


def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento

ciudades_devueltas=devuelveCiudades("Madrid","Barcelona","Valencia","Bilbao")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))