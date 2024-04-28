from Conexion import *

class CClientes:
    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado


        except mysql.connector.Error as err:
            print("Error de mostrar de datos: {}".format(err))
    def IngresarClientes(nombres, apellidos, sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,) la coma hace que sea una tupla
            #Las tuplas son listas inmutables, no se puede modificar

            valores = (nombres, apellidos, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registros ingresado")
            cone.close()


        except mysql.connector.Error as err:
            print("Error de ingreso de datos: {}".format(err))
