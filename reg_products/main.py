from tkinter import *
from tkinter import messagebox as mb
import sqlite3

# ------------------------------------------------------------


def crearBase():
    try:
        conexion = sqlite3.connect("reg_productsdb")
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE PRODUCTOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_ARTICULO VARCHAR(50),
                PRECIO INTEGER,
                CATEGORIA VARCHAR(20))
            """
        )
    except:
        mb.showwarning("Base de datos", "La base de datos ya ha sido creada")


def agregarProducto():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    try:
        if elNombre.get()!='' and elPrecio.get()!='' and elCat.get()!='':
            if elID.get()=='':
                cursor.execute( "INSERT INTO PRODUCTOS VALUES(NULL,'"+ boxNombre.get()+ "','"+ boxPrecio.get() + "','"+ boxCat.get()+ "')")
                elID.set(cursor.lastrowid)
                mb.showinfo("Creado","ID: '"+elID.get()+"'\nNombre: '"+elNombre.get()+"'\nPrecio: '"+elPrecio.get()+"'\nCategoria: '"+elCat.get()+"'")
            else:
                cursor.execute("SELECT * FROM PRODUCTOS WHERE ID='"+boxId.get()+"'")
                existe=cursor.fetchall()
                if existe!=[]:
                    mb.showerror("Ya existe","Ya existe un producto con ese ID\nDejar en blanco para AutoID")
                else:
                    cursor.execute( "INSERT INTO PRODUCTOS VALUES('"+ elID.get()+ "','"+ elNombre.get()+ "','"+ elPrecio.get() + "','"+ elCat.get()+ "')")
                    elID.set(cursor.lastrowid)
                    mb.showinfo("Creado","ID: '"+elID.get()+"'\nNombre: '"+elNombre.get()+"'\nPrecio: '"+elPrecio.get()+"'\nCategoria: '"+elCat.get()+"'")
        else:
            mb.showerror("Error","Rellene los campos Nombre-Precio-Categoria")
    except sqlite3.IntegrityError:
        mb.showerror("Error","El ID debe ser numerico")
    
    conexion.commit()

def borrarProducto():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    consultarProducto()
    if elNombre.get()=='':
        pass
    else:
        ask = mb.askquestion("Borrar producto","Desea borrar el producto '"+boxId.get()+"'?")
        if ask=='yes':
            cursor.execute("DELETE FROM PRODUCTOS WHERE ID='"+boxId.get()+"'")
            elID.set('')
            elNombre.set('')
            elPrecio.set('')
            elCat.set('')
        else:
            pass
    conexion.commit()

def actualizarProducto():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    ask = mb.askquestion("Actualizar","Desea actualizar el producto '"+boxId.get()+"'?")
    if ask=='yes':
        cursor.execute("UPDATE PRODUCTOS SET NOMBRE_ARTICULO='"+ elNombre.get()+ "', PRECIO='"+ elPrecio.get() + "', CATEGORIA='"+ elCat.get()+ "' WHERE ID='"+elID.get()+"'")
        mb.showinfo("Actualizado","ID: '"+elID.get()+"'\nNombre: '"+elNombre.get()+"'\nPrecio: '"+elPrecio.get()+"'\nCategoria: '"+elCat.get()+"'")
    else:
            pass
    conexion.commit()

def consultarProducto():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PRODUCTOS WHERE ID='"+elID.get()+"'")
    producto=cursor.fetchall()
    
    if producto==[]:
        mb.showerror("ID Prodcuto","No existe un producto con esa ID")
        elNombre.set('')
        elPrecio.set('')
        elCat.set('')
    else:
        for producto in producto:
            elNombre.set(producto[1])
            elPrecio.set(producto[2])
            elCat.set(producto[3])
    conexion.commit()

def consultarID():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PRODUCTOS WHERE ID='"+boxId.get()+"'")
    idBuscado=cursor.fetchall()
    if idBuscado==[]:
        return True
    else:
        return False

def borrarCampos():
    elID.set('')
    elNombre.set('')
    elPrecio.set('')
    elCat.set('')

def salirPrograma():
    preg=mb.askyesno("Salir","Desea salir del programa?")
    if preg==True:
        root.destroy()
    else:
        pass

'''def imprimirProductos():
    conexion = sqlite3.connect("reg_productsdb")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PRODUCTOS")
    todos=cursor.fetchall()
    print(todos)
    conexion.commit()'''
# ------------------------------------------------------------
root = Tk()
root.title("Registro de productos")
root.resizable(0, 0)
root.iconbitmap('tech.ico')
miFrame = Frame(root)
miFrame.pack()
# ------------------------------MENU-------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoBBDD = Menu(barraMenu, tearoff=0)
archivoBBDD.add_command(label="Conectar Base", command=crearBase)
#archivoBBDD.add_command(label="Ver Productos", command=imprimirProductos)
archivoBBDD.add_command(label="Salir",command=salirPrograma)


archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca")

barraMenu.add_cascade(label="Base de Datos", menu=archivoBBDD)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
#------------------------------STRINGVAR
elID=StringVar()
elNombre=StringVar()
elPrecio=StringVar()
elCat=StringVar()

# -----------------------------ID--------------------------
labelId = Label(miFrame, text="ID:")
labelId.grid(row=0, column=0, padx=10, pady=10)
boxId = Entry(miFrame,textvariable=elID)
boxId.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
# -----------------------------NOMBRE--------------------------

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, padx=10, pady=10)
boxNombre = Entry(miFrame,textvariable=elNombre)
boxNombre.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
# -----------------------------PRECIO--------------------------

labelPrecio = Label(miFrame, text="Precio:")
labelPrecio.grid(row=2, column=0, padx=10, pady=10)
boxPrecio = Entry(miFrame,textvariable=elPrecio)
boxPrecio.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
# -----------------------------CATEGORIA--------------------------

labelCat = Label(miFrame, text="Categoria:")
labelCat.grid(row=3, column=0, padx=10, pady=10)
boxCat = Entry(miFrame,textvariable=elCat)
boxCat.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
# -----------------------------BOTONES--------------------------

miFrame2 = Frame(root)
miFrame2.pack()

botonAgregar = Button(miFrame, text="CC", command=borrarCampos)
botonAgregar.grid(row=4, column=1, padx=5, pady=5)

botonAgregar = Button(miFrame, text="Agregar", command=agregarProducto)
botonAgregar.grid(row=4, column=2, padx=5, pady=5)

botonEliminar = Button(miFrame, text="Eliminar",command=borrarProducto)
botonEliminar.grid(row=4, column=3, padx=5, pady=5)

botonModificar = Button(miFrame, text="Modificar",command=actualizarProducto)
botonModificar.grid(row=4, column=4, padx=5, pady=5)

botonConsulta = Button(miFrame, text="Consultar ID",command=consultarProducto)
botonConsulta.grid(row=4, column=5, padx=5, pady=5)


root.mainloop()