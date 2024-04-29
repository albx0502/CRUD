Ejercicio de CRUD utilizando Python y mysql.
Para usarlo debes ir a la clase Conexion.py y ahi introducir los datos pertenecientes a tu base de datos, como tu contraseña, usuario, el nombre de la base de datos.
Tambien deberas crear una base de datos con el nombre que hayas elegido, usando herramientas como mysql workbench usando el comando CREATE DATABASE nombre_de_la_base_de_datos; y USE nombre_de_la_base_de_datos;
Ademas de crear una tabla con este comando (si quisieses se puede cambiar el nombre y los datos pero se tendrian que cambiar correspondientemente en las clases de Python) 
CREATE TABLE usuarios(
id int auto_increment primary key not null,
nombres varchar(50),
apellidos varchar(50),
sexo varchar(30)
)
Ademas deberas usar el comando de Python pip en la linea de comandos para instalar los paquetes de mysql-connector y tkinter, usando el comando pip install nombre_del_paquete.
