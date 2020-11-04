from tkinter import *

root = Tk()
root.title("Ejemplo")

# cMAL

filepath = "/Users/maria/avion2.png"
foto = Image.open(filepath).resize((100, 150), Image.ANTIALIAS)
foto = root.PhotoImage(foto)
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa").pack()
Checkbutton(frame, text="Desierto").pack()
Checkbutton(frame, text="Montaña").pack()

root.mainloop()