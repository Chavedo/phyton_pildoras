mitupla=("Juan",13,1995,13)
milista=list(mitupla) #tuple convierte tupla en lsita, 
                      #tuple para lo contrario
print(mitupla[2])
print(mitupla) #se ve entre parentesis
print(milista) #se ve entre corchetes
print("Juan" in mitupla) # vertifica si existe juan en la tupla
print(mitupla.count(13)) #cuantas veces esta el element en la tupla
print(len(mitupla)) #cuantos elemenos hay 

#desempaquetado de tuplas
nombre, dia, mes, agno=mitupla
print(nombre)
print(dia)
print(agno)
print(mes)

#buscar por index
print(mitupla.index(13))