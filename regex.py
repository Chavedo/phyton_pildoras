import re

cadena="Vamos a aprender expresiones regulares"

#print(re.search("aprender",cadena))

textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
    print("Aca ta")
else:
    print("No ta")

