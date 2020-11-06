import math
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Calculadora")
miFrame = Frame(root)
miFrame.pack()

# DECLARACION DE V.GLOBALES
operacion = ""
resultado = 0

# -----pantalla

numeroPantalla = StringVar(value="0")

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# --------pulsacion teclado----------


def numeroPulsado(num):
    if num == ".":
        if numeroPantalla.get() == "0":
            numeroPantalla.set(numeroPantalla.get() + num)
        elif numeroPantalla.get() == ".":
            numeroPantalla.set(0)
        else:
            if "." in numeroPantalla.get():
                numeroPantalla.set(numeroPantalla.get())
            else:
                numeroPantalla.set(numeroPantalla.get() + num)
    else:
        if numeroPantalla.get() == "0":
            numeroPantalla.set(num)
        else:
            numeroPantalla.set(numeroPantalla.get() + num)


def borrarNumero():
    i = numeroPantalla.get()
    if len(i) > 1:
        numeroPantalla.set(numeroPantalla.get()[0:-1])
    else:
        numeroPantalla.set(0)


def borrarTodo():
    global resultado
    global operacion
    resultado = 0
    operacion = ""
    numeroPantalla.set(0)


# ------------FUNCION RESULTADO
def igual(num):
    global resultado
    global operacion

    if operacion == "suma":
        resultado = resultado + float(num)
    elif operacion == "resta":
        resultado = resultado - float(num)
    elif operacion == "multi":
        resultado = resultado * float(num)
    elif operacion == "div":
        try:
            resultado = resultado / float(num)
        except ZeroDivisionError:
            mb.showerror("Division", "No se puede dividir por cero")
    elif operacion == "pot":
        resultado = resultado ** float(num)
    elif operacion == "sqrt":
        resultado = float(num) ** (1.0 / resultado)

    operacion = ""
    numeroPantalla.set(round(resultado, 2))


# ---------FUNCION SUMA
def suma(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "suma"

    numeroPantalla.set("0")


# -----------FUNCION RESTA
def resta(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "resta"

    numeroPantalla.set("0")


# -----------FUNCION MULTIPLICACION
def multiplicar(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "multi"

    numeroPantalla.set("0")


# -----------FUNCION DIVIDIR
def dividir(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "div"

    numeroPantalla.set("0")


# -----------FUNCION POTENCIA
def potencia(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "pot"

    numeroPantalla.set("0")


# -----------FUNCION RAIZ
def raiz(num):

    global operacion
    global resultado

    resultado = float(num)
    operacion = "sqrt"

    numeroPantalla.set("0")


# -----fila0-----
botonraiz = Button(
    miFrame,
    text="√",
    width="10",
    height="2",
    command=lambda: raiz(numeroPantalla.get()),
)
botonraiz.grid(row=1, column=1)
botonraiz.config(background="gray", fg="black", justify="center")

botonpotencia = Button(
    miFrame,
    text="^",
    width="10",
    height="2",
    command=lambda: potencia(numeroPantalla.get()),
)
botonpotencia.grid(row=1, column=2)
botonpotencia.config(background="gray", fg="black", justify="center")

botonclearall = Button(
    miFrame, text="CE", width="10", height="2", command=lambda: borrarTodo()
)
botonclearall.grid(row=1, column=3)
botonclearall.config(background="gray", fg="red", justify="center")

botonclear = Button(
    miFrame, text="C", width="10", height="2", command=lambda: borrarNumero()
)
botonclear.grid(row=1, column=4)
botonclear.config(background="gray", fg="black", justify="center")

# -----fila1---------------------
boton7 = Button(
    miFrame, text="7", width="10", height="2", command=lambda: numeroPulsado("7")
)
boton7.grid(row=2, column=1)
boton7.config(background="gray", fg="black", justify="center")

boton8 = Button(
    miFrame, text="8", width="10", height="2", command=lambda: numeroPulsado("8")
)
boton8.grid(row=2, column=2)
boton8.config(background="gray", fg="black", justify="center")

boton9 = Button(
    miFrame, text="9", width="10", height="2", command=lambda: numeroPulsado("9")
)
boton9.grid(row=2, column=3)
boton9.config(background="gray", fg="black", justify="center")

botondiv = Button(
    miFrame,
    text="/",
    width="10",
    height="2",
    command=lambda: dividir(numeroPantalla.get()),
)
botondiv.grid(row=2, column=4)
botondiv.config(background="gray", fg="black", justify="center")

# -----fila2
boton4 = Button(
    miFrame, text="4", width="10", height="2", command=lambda: numeroPulsado("4")
)
boton4.grid(row=3, column=1)
boton4.config(background="gray", fg="black", justify="center")

boton5 = Button(
    miFrame, text="5", width="10", height="2", command=lambda: numeroPulsado("5")
)
boton5.grid(row=3, column=2)
boton5.config(background="gray", fg="black", justify="center")

boton6 = Button(
    miFrame, text="6", width="10", height="2", command=lambda: numeroPulsado("6")
)
boton6.grid(row=3, column=3)
boton6.config(background="gray", fg="black", justify="center")

botonmulti = Button(miFrame, text="X", width="10", height="2")
botonmulti.grid(row=3, column=4)
botonmulti.config(
    background="gray",
    fg="black",
    justify="center",
    command=lambda: multiplicar(numeroPantalla.get()),
)

# -----fila3
boton1 = Button(
    miFrame, text="1", width="10", height="2", command=lambda: numeroPulsado("1")
)
boton1.grid(row=4, column=1)
boton1.config(background="gray", fg="black", justify="center")

boton2 = Button(
    miFrame, text="2", width="10", height="2", command=lambda: numeroPulsado("2")
)
boton2.grid(row=4, column=2)
boton2.config(background="gray", fg="black", justify="center")

boton3 = Button(
    miFrame, text="3", width="10", height="2", command=lambda: numeroPulsado("3")
)
boton3.grid(row=4, column=3)
boton3.config(background="gray", fg="black", justify="center")

botonmenos = Button(
    miFrame,
    text="-",
    width="10",
    height="2",
    command=lambda: resta(numeroPantalla.get()),
)
botonmenos.grid(row=4, column=4)
botonmenos.config(background="gray", fg="black", justify="center")

# -----fila4
boton0 = Button(
    miFrame, text="0", width="10", height="2", command=lambda: numeroPulsado("0")
)
boton0.grid(row=5, column=1)
boton0.config(background="gray", fg="black", justify="center")

botoncoma = Button(
    miFrame, text=".", width="10", height="2", command=lambda: numeroPulsado(".")
)
botoncoma.grid(row=5, column=2)
botoncoma.config(background="gray", fg="black", justify="center")

botonigual = Button(
    miFrame,
    text="=",
    width="10",
    height="2",
    command=lambda: igual(numeroPantalla.get()),
)
botonigual.grid(row=5, column=3)
botonigual.config(background="gray", fg="black", justify="center")

botonmas = Button(miFrame, text="+", width="10", height="2")
botonmas.grid(row=5, column=4)
botonmas.config(
    background="gray",
    fg="black",
    justify="center",
    command=lambda: suma(numeroPantalla.get()),
)


root.mainloop()
