# -*- coding: cp1252 -*-
import sqlite3 as dbapi


class TerremotosBBDD:

        def __init__(self, fich_bd):
                self.__fich_bd=fich_bd


        def vaciar(self):
                sql = """delete from terremotos"""
                try:
                        bbdd = dbapi.connect(self.__fich_bd)
                        cursor = bbdd.cursor()
                        cursor.execute(sql)
                        bbdd.commit()
                        
                except Exception as e:
                        print (e)
                        
                finally:
                        cursor.close()
                        bbdd.close()
                

        def importar(self, fich):
                # Recibe el nombre del fichero a importar:
                sql_base = "insert into terremotos values(?,?,?,?,?)"
                num = 0
                try:
                        bbdd = dbapi.connect(self.__fich_bd)
                        cursor = bbdd.cursor()
                        f = open(fich, "r")
                        while True:
                                linea = f.readline()
                                if not linea:
                                        break
                                else:
                                        # insertar los registros en la BD:
                                        linea = linea[:-1]
                                        print (linea)

                                        if linea != "":
                                                cols = linea.split(";")
                                                #print cols
                                                #print tuple(cols)
                        
                                                # ejecutar la consulta:        
                                                cursor.execute(sql_base, tuple(cols))

                                                # confirmar la transacción:
                                                bbdd.commit()
                                                num += 1
                        return num
                
                except Exception as e:
                        print (e)
                
                finally:                
                        f.close()
                        cursor.close()
                        bbdd.close()
                

        def exportar(self, fich):
                # Recibe el nombre del fichero a exportar:
                sql = "select * from terremotos"
                num = 0
                
                try:
                        bbdd = dbapi.connect(self.__fich_bd)
                        cursor = bbdd.cursor()
                        f = open(fich,"w")

                        cursor.execute(sql)
                        for tupla in cursor.fetchall():                         
                                s = ";".join(tupla) + "\n"                       
                                f.writelines(s)
                                num += 1
                                
                        return num
                
                except Exception as e:
                        print (e)
                        
                finally:
                        f.close()
                        cursor.close()
                        bbdd.close()


# codigo principal:

bbdd = TerremotosBBDD("terremotos.dat")

bbdd.vaciar()
print ("Tabla inicializada")

numLineas = bbdd.importar("terremotos.csv")
print ("Numero de lineas importadas: " + str(numLineas))

numLineas = bbdd.exportar("terremotos_out.csv")
print ("Numero de lineas exportadas: " + str(numLineas))
