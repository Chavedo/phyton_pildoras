import sqlite3


miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# si se ejecuta va a dar error porq ya existe esa tabla

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

"""variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
"""
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print("Nombre articulo:", producto[0], "| Seccion:", producto[2])


miConexion.commit()


miConexion.close()