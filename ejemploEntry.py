from tkinter import *
import tkinter.scrolledtext as scrolledtext

raiz=Tk()
raiz.title("ejemploEntry")

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show='*')

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

textoComentario=scrolledtext.ScrolledText(miFrame,width=13,height=10)
textoComentario.grid(row=4,column=1, pady = 10, padx = 10)

'''textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=10)'''


nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():

    minombre.set("Juan")

botonEnvio=Button(raiz,text='Enviar',command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()