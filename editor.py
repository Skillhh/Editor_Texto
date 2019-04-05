#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog as FileDialog
from io from open

ruta = ""

def nuevo():
	global ruta
	mensaje.set("Nuevo fichero")
	ruta = ""
	texto.delete(1.0, "end")
	root.title("Editor")

def abrir():
	global ruta
	mensaje.set("Abrir fichero")
	ruta = FileDialog.askopenfilename(
		initialdir='.', 
		filetype=(("Ficheros de Texto","*.txt"),), 
		title = "Abrir Fichero de Texto")
	if ruta != "":
		fichero = open(ruta, 'r')
		contenido = fichero.read()
		texto.delete(1.0, "end")
		texto.insert("insert", contenido)
		fichero.close()
		root.title(ruta + " - Editor")

def guardar():
	mensaje.set("Guardar fichero")

def guardar_como():
	mensaje.set("Guardar como")


# Configuracion Raiz
root = Tk()
root.title("Editor")

#Menu de fichero
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu , label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Mono", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")

monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side='left')


root.config(menu=menubar)

root.mainloop()
