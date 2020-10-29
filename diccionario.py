'''midiccionario={"Alemania":"Berlín","Francia":"París","Argentina":"Buenos Aires","España":"Madrid"}
midiccionario["Italia"]="Roma" #agregar otro clave valor
#print(midiccionario["Francia"])
print(midiccionario)
del midiccionario["Argentina"]
print(midiccionario)

mitupla="España","Francia","Argentina","Alemania"
midic={mitupla[0]:"Madrid",mitupla[1]:"Londres"}
print(midic)'''

midiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1998]}}
print(midiccionario)
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))
print(midiccionario["anillos"])