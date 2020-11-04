from tkinter import *
from tkinter import filedialog as fd

root = Tk()


def abreFichero():

    fichero = fd.askopenfilename(
        title="Abrir",
        initialdir="C:",
        filetypes=(
            ("Ficheros de Excel", "*.xlsx"),
            ("Ficheros de texto", "*.txt"),
            ("Todos los ficheros", ("*.*")),
        ),
    )

    print(fichero)


Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()