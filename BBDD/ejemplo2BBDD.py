import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute(
    """
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY autoincrement,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))   
"""
)

productos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria"),
    ("Destornillador", 45, "Ferreteria"),
]


# miCursor.execute('INSERT INTO PRODUCTOS VALUES("AR03","Tren", 155, "Jugueteria")')
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)", productos)


miConexion.commit()
miConexion.close()