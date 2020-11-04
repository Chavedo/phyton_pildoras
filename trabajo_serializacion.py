import pickle

'''lista_nombres=["Mariano","Pedro","Ana","Maria"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del(fichero_binario)'''

fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)