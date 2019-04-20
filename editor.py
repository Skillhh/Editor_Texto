from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

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
		title="Abrir Fichero de Texto", 
		initialdir=".", 
		filetypes=(("Ficheros de Texto", "*.txt"),
			("Ficheros Python", "*.py"),)	
		)

	if ruta != "":
		fichero = open(ruta, 'r+')
		contenido = fichero.read()
		texto.delete(1.0, "end")
		texto.insert("insert", contenido)
		fichero.close()
		root.title(ruta + " - Editor")


def guardar():
	mensaje.set("Guardar fichero")
	if ruta != "":
		contenido = texto.get(1.0, "end-1c")
		fichero = open(rute, "w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Se ha guardado correctamente.")
	else:
		guardar_como()

def guardar_como():
	global ruta
	mensaje.set("Guardar como")
	fichero = FileDialog.asksaveasfile(
		title="Guardar Como",
		mode="w",
		defaultextension="*.txt"
	)
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0, "end-1c")
		fichero = open(ruta, "w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Se ha guardado correctamente.")
	else:
		mensaje.set("Guardado Cancelado")
		ruta = ""

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
