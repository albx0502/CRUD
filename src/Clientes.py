from Conexion import *

class CClientes:
    def IngresarClientes(nombres, apellidos, sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s);"
            #La variable valores tiene que ser una tupla



        except mysql.connector.Error as err:
            print("Error de ingreso de datos: {}".format(err))
