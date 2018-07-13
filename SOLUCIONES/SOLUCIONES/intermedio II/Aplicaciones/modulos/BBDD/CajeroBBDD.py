import sqlite3 as bdapi

from ..objetos.Cajero import *

class CajeroBBDD(object):

        def __init__(self,ficheroBBDD):                
                self.__bd = bdapi.connect(ficheroBBDD)
                self.__cursor = self.__bd.cursor()
        
        def actualizar(self, cajero):
                """ Actualizar la BBDD con los datos del cajero"""
                sql="""update cajero set b500=?,b200=?,b100=?,b50=?,b20=?,b10=?"""
                self.__cursor.execute(sql,cajero.getTuplaBilletes())
                self.__bd.commit()
                
                                      
        def cargar(self):
                """ Devuelve un cajero inicializado con los billetes de la BBDD"""
                dictCajero = {}                
                
                sql="""select * from cajero"""
                self.__cursor.execute(sql)
                t = self.__cursor.fetchone()
                               
                if t != None:                        
                        L = [int(i[0][1:]) for i in self.__cursor.description]
                        
                        for i in range(0,len(t)):
                                billete = L[i]
                                cantidad = t[i]
                                dictCajero[billete]=cantidad
                                
                return Cajero(dictCajero)                       
                                

        def desconectar(self):
                """Cierra conexion con la BD"""
                if self.__cursor:
                        self.__cursor.close()

                if self.__bd:
                        self.__bd.close()

