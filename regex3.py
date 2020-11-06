import re

lista_nombres=[
    'Ana','Pedro','Maria','Rosa','Sandra','Celia'
]

#print(re.search("aprender",cadena))

textoBuscar="aprender"

for elemento in lista_nombres:
    if re.findall('[o-t]$',elemento):
        print(elemento)

