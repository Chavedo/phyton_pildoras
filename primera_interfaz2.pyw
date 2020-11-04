from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)

raiz.iconbitmap("tech.ico")

raiz.geometry("650x350")

raiz.config(bg="gray")

miFrame=Frame()

miFrame.pack()#fill="y",expand="True"

miFrame.config(bg="black")

miFrame.config(width="450",height="350")

miFrame.config(bd="14")

miFrame.config(relief="groove")

miFrame.config(cursor="hand2")

raiz.mainloop()
