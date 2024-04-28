# pip install mysql-connector
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',
                                               password='almu1964',
                                               host='localhost',
                                               database='clientesdb',
                                               port=3306)
            print("Conexion Correcta")

            return conexion


        except mysql.connector.Error as err:
            print("Error al conectar con la base de datos {}".format(err))

            return conexion

    ConexionBaseDeDatos()