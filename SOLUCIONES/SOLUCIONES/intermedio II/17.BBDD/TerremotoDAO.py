import sqlite3 as dbapi

class Terremoto:

        def __init__(self, evento, fecha, hora, latitud, longitud):
                self.__evento = evento
                self.__fecha = fecha
                self.__hora = hora
                self.__latitud = latitud
                self.__longitud = longitud

        def __str__(self):
                return self.__evento + " " + self.__fecha + " " + self.__hora + " " + self.__latitud + " " + self.__longitud

        def toCSV(self):
                return self.__evento + ";" + self.__fecha + ";" + self.__hora + ";" + self.__latitud.replace(".",",") + ";" + self.__longitud.replace(".",",")

        def getTupla(self):
                return (self.__evento,self.__fecha,self.__hora ,self.__latitud,self.__longitud)
                

class TerremotoDAO:
        

        def __init__(self, fich_bd):
                self.__bbdd = dbapi.connect(fich_bd)
                self.__cursor = self.__bbdd.cursor()

        def create(self,t):
                self.__cursor.execute("""insert into terromotos values(?,?,?,?,?)""", t.getTupla())
                self.__bbdd.commit()

        def delete(self, dni):
                self.__cursor.execute("""delete from terromotos where dni = ?""", (dni,))
                self.__bbdd.commit()

        def update(self, empleado):
                t = (empleado.nombre, empleado.departamento, empleado.dni)
                self.__cursor.execute("""update empleados set nombre = ?, departamento = ? where dni = ?""", t)
                self.__bbdd.commit()

        def read(self, dni):
                 self.__cursor.execute("""select * from empleados where dni = ?""", (dni,))
                 t = self.__cursor.fetchone()
                 return Empleado(t[0],t[1],t[2])

        
        def readall(self):
                 self.__cursor.execute("""select * from empleados""")
                 L = []
                 for t in self.__cursor.fetchall():
                         L.append(Empleado(t[0],t[1],t[2]))
                 return L

        def close(self):
                if self.__cursor != None:
                        self.__cursor.close()
                        
                if self.__bbdd != None:
                        self.__bbdd.close()
