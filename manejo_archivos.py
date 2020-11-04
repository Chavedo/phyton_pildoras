from io import open
'''
archivo_texto=open("archivo.txt", "w")

frase="Estupendo para estudiar phyton"

archivo_texto.write(frase)

archivo_texto.close()'''

 archivo_texto=open("archivo.txt", "r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)