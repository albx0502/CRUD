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





            base.mainloop()


        except ValueError as error:
            print("Error al mostrar la Interfaz,error: {}".format(error))

    Formulario()