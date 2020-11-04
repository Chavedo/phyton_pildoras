from io import open

arch=open("archivo.txt","r+")

lista_texto=arch.readlines()

lista_texto[1]=" Esta linea ha sido incluida desde el exterior \n  "

arch.seek(0)
arch.writelines(lista_texto)
arch.close()