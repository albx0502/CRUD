import tkinter as tk

#importat los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *


class formularioClientes:
    global base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxNombres
    textBoxNombres = None

    global textBoxApellidos
    textBoxApellidos = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None



def Formulario():

        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global combo
        global groupBox
        global tree
        global base

        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")

            groupBox = LabelFrame(base, text="Datos del Personal", padx=5,pady=5)
            groupBox.grid(column=0, row=0,padx=10,pady=10)

            labelId = Label(groupBox, text="Id:",width=13,font="arial 12 ").grid(row=0,column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0,column=1)

            labelNombres = Label(groupBox, text="Nombres:", width=13, font="arial 12 ").grid(row=1, column=0)
            textBoxNombres = Entry(groupBox)
            textBoxNombres.grid(row=1, column=1)

            labelApellidos = Label(groupBox, text="Apellidos:", width=13, font="arial 12 ").grid(row=2, column=0)
            textBoxApellidos = Entry(groupBox)
            textBoxApellidos.grid(row=2, column=1)

            labelSexo = Label(groupBox, text="Sexo:", width=13, font="arial 12 ").grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino","Prefiero no decirlo"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=4, column=0)
            Button(groupBox, text="Modificar", width=10).grid(row=4, column=1)
            Button(groupBox, text="Eliminar", width=10).grid(row=4, column=2)


            groupBox = LabelFrame(base, text="Lista del Personal", padx=5,pady=5,)
            groupBox.grid(column=1, row=0,padx=5,pady=5)
            #Crear un Treeview

            #Configurar las columnas

            tree = ttk.Treeview(groupBox, columns=("Id","Nombres","Apellidos","Sexo"), show="headings", height=5)
            tree.column("#1", anchor="center")
            tree.heading("#1", text="Id")
            tree.column("#2", anchor="center")
            tree.heading("#2", text="Nombres")
            tree.column("#3", anchor="center")
            tree.heading("#3", text="Apellidos")
            tree.column("#4", anchor="center")
            tree.heading("#4", text="Sexo")

            #agregar los datos a la tabla
            #mostrar la tabla

            for row in CClientes.mostrarClientes():
                tree.insert("", "end", values=row)


            tree.pack()


            base.mainloop()


        except ValueError as error:
            print("Error al mostrar la Interfaz,error: {}".format(error))

def guardarRegistros():
        global textBoxNombres, textBoxApellidos, combo, groupBox

        try:
            #Verificar si los widgets estan inicializados
            if textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            nombres = textBoxNombres.get()
            apellidos = textBoxApellidos.get()
            sexo = combo.get()

            CClientes.IngresarClientes(nombres, apellidos, sexo)
            messagebox.showinfo("Informacion","Los datos fueron guardados")

            actualizarTreeView()

            #Limpiamos los campos
            textBoxNombres.delete(0, END)
            textBoxApellidos.delete(0, END)

        except ValueError as error:
            print("Error al ingresar los datos,error: {}".format(error))

def actualizarTreeView():
    global tree

    try:
        #borrar todos los elementos actuales del TreeView
        tree.delete(*tree.get_children())
        #obtener los nuevos datos que tenemos que mostrar
        datos = CClientes.mostrarClientes()

        #insertar los nuevos datos en el treview
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)


    except ValueError as error:
        print("Error al actualizar la tabla, error: {}".format(error))

Formulario()