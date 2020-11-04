from tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)

miFrame.pack()

miImagen=PhotoImage(file="image.png")

Label(miFrame, image=miImagen).place(x=100,y=200)

root.mainloop()