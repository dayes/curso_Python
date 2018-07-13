# Crear un empleado con el SQL:
# insert into empleados(dni,nombre,departamento) values
# ('484838848R','AAAA','DPO')

import sqlite3 as dbapi


# 1) Abrir una conexion:
conexion = dbapi.connect("bbdd.dat")

# 2) Coger un cursor de la conexion:
cursor = conexion.cursor()

# 3) SQL: 
sql = "insert into empleados(dni,nombre,departamento) values(?,?,?)"

# 4) Ejecutar la query con el cursor
cursor.execute(sql, ('12345678A','Juan Martinez','RRHH'))

# 5) Transacciones:
resp = input("Confirmar S o N: ")
if resp == 'S':
	conexion.commit()  # Confirmar los cambios
else:
	conexion.rollback() # NO grabamos los cambios

# 6) Liberar recursos:
cursor.close()
conexion.close()
