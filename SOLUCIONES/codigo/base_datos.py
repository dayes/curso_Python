import sqlite3 as dbapi

# listar empleados de un departamento:
departamento = input('Teclear un departamento:')

# 1) Abrir una conexion:
conexion = dbapi.connect("bbdd.dat")

# 2) Coger un cursor de la conexion:
cursor = conexion.cursor()

# 3) SQL: select * from empleados
sql = "select * from empleados where departamento=?"

# 4) Ejecutar la query con el cursor
cursor.execute(sql, (departamento,))

# 5) Iterar por los resultados:
for dni,nom, dpo in cursor.fetchall():
	print(dni, nom, dpo)
	
# 6) Liberar recursos:
cursor.close()
conexion.close()
