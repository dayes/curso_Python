# IMPRIMIR MI PROPIO FICHERO:
IMPORT SYS
NOMBREFICH = SYS.ARGV[0]
F = NONE
F2 = NONE
PRINT(NOMBREFICH)
NOMBREFICH2 = "COPIA DE " + NOMBREFICH
TRY:
	# ABRIR FICHERO
	F = OPEN(NOMBREFICH, "R") # ABRIR PARA LEER
	F2 = OPEN(NOMBREFICH2, "W") # ABRIR PARA ESCRIBIR
	WHILE TRUE:
		LINEA = F.READLINE()
		IF NOT LINEA: BREAK
		
		LINEA = LINEA.STRIP('\N')
		IF LEN(LINEA) > 0:
			PRINT(LINEA)
			F2.WRITE(LINEA.UPPER()+'\N')
						
EXCEPT IOERROR AS E:
	PRINT('ERROR:',E)
	
FINALLY:
	IF F != NONE:
		F.CLOSE()
	IF F2 != NONE:
		F2.CLOSE()	
		