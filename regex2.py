import re

lista_nombres = [
    "Ana Gomez",
    "Santiago Martin",
    "Maria Martin",
    "Sandra Fernandez",
    "Sandra Lopez",
    "Celia",
]

for elemento in lista_nombres:
    if re.findall("^Sandra", elemento):
        print(elemento)