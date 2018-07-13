#-*- coding: cp850 -*-

import re
try:
	import urllib2
except:
	import urllib.request as urllib2	

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


class TerremotoWeb:
        
        def __init__(self, n=10, traza=False):
                self.__n = n;
                self.__traza = traza
                self.__lista = []
                self.__download()

        def getList(self):
                return self.__lista
        

        def save(self, fichero):
                f = open(fichero, "w")
                
                for t in self.__lista:
                        f.writelines(t.toCSV()+"\n")
                f.close()                        
                
        def __download(self):                                

                
                URL="http://www.ign.es/ign/layoutIn/sismoListadoTerremotos.do?zona=1&cantidad_dias=10"

                f = urllib2.urlopen(URL)
                html = f.read()
                f.close()

                #print (html)
                

                i=0

                for match in re.finditer(b'<tr class="filaNegra2">(.*?)</tr>', html,re.DOTALL):                
                        linea = match.group(0)
                        #print (linea)


                        # Solo interesan las primeras 5 cols:
                        fila = []
                        j=0
                        
                        for match2 in re.finditer(b'<td.*?>(.*?)</td>', linea,re.DOTALL):
                                s = match2.group(1).decode('cp850')
                                fila += [s]
                                j+=1
                                if j==5:
                                        break
											

                        #Imprime la lista:
                        if self.__traza == True:
                                print (fila)

                        t = Terremoto(fila[0],fila[1],fila[2],fila[3],fila[4])
                        self.__lista += [t]
												
                        #Control del numero de fila
                        i+=1
                        if i==self.__n:
                                break
                        
                

# principal:
#try:
n = 5
tt = TerremotoWeb(n)
L = tt.getList()

print ("\nListado de los ",n," primeros Terremotos:")
for t in L:
		print (t)

tt.save("terremotos.csv")                

#except Exception as e:
#        print ("ERROR: ", e)
