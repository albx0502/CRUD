import tkinter as tk

#importat los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox


class formularioClientes:
    def Formulario():
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
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=1, column=1)

            labelApellidos = Label(groupBox, text="Apellidos:", width=13, font="arial 12 ").grid(row=2, column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=2, column=1)

            labelSexo = Label(groupBox, text="Sexo:", width=13, font="arial 12 ").grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino","Prefiero no decirlo"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox, text="Guardar", width=10).grid(row=4, column=0)
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

            tree.pack()


            base.mainloop()


        except ValueError as error:
            print("Error al mostrar la Interfaz,error: {}".format(error))

    Formulario()