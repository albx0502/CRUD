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

            base.mainloop()


        except ValueError as error:
            print("Error al mostrar la Interfaz,error: {}".format(error))

    Formulario()