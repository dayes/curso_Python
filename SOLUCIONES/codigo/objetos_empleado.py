# clases Empleado:

class EmpleadoError(Exception):
	
	def _init__(self, msg):
		super().__init__(msg)
		

class Empleado(object):
	
	# variable estatica:
	__numEmpleados = 0
	
	def __init__(self,nombre="",empresa="",sueldo=0.0):
		if sueldo < 1000:
			raise EmpleadoError('Sueldo incorrecto...')
			
		self.__nombre = nombre
		self.__empresa = empresa
		self.__sueldo = sueldo
		self.__proyectos = []
		
		# cada vez que creamos un empleado
		# se suma uno a la var. estatica:
		Empleado.__numEmpleados+=1
		
	def getNombre(self):
		return self.__nombre
		
	def setNombre(self, nombre):
		self.__nombre = nombre
		
	@staticmethod
	def numeroDeEmpleados():
		return Empleado.__numEmpleados		
	
	def asignarProyecto(self, *proyectos):
		for p in proyectos:
			self.__proyectos.append(p)
		
	def __str__(self):
		return self.__nombre+' '+self.__empresa+' '+ \
		 str(self.__sueldo)+' '+ str(self.__proyectos)
		 
	def __repr__(self):
		return self.__nombre+' '+self.__empresa+' '+ \
		 str(self.__sueldo)+' '+ str(self.__proyectos)
		 
class JefeDeProyecto(Empleado):
	
	def __init__(self,nombre="",empresa="",sueldo=0.0,empleados=[]):
		Empleado.__init__(self,nombre,empresa,sueldo)
		self.__empleados = empleados
		
	def __str__(self):
		return super().__str__() + ' '+ str(self.__empleados)
		
	def __repr__(self):
		return super().__repr__() + ' '+ repr(self.__empleados)
		
		
class Analista(Empleado):
	pass
		
if __name__ == '__main__':
	
	emp1 = Empleado('Sara','CEE',3000.0)
	print('Nombre del empleado: ',emp1.getNombre())
	emp1.setNombre('Sara Gonzalez')
	print('Nombre del empleado: ',emp1.getNombre())
	
	jp = JefeDeProyecto('Sara','CEE',3000.0,['Miguel','Eva'])
	#print('Att nombre: ', jp.__nombre)
	print('Clase:', jp.__class__.__name__)
	
	print('DIC',jp.__dict__)
	jp.__dict__['otro']=100 # Agregamos un att. en t.ejecucion
	print('DIC',jp.__dict__)
	
	
	nombreAtt = 'nombre2'
	if hasattr(jp, nombreAtt):
		print('Tiene el att ',nombreAtt)
	else:
		print('No lo tiene')
	
	jp.asignarProyecto('Intranet')
	jp2 = JefeDeProyecto('Juan','CSS',2700.0,['Jose'])
	print('DIC 2',jp2.__dict__)
	L = [jp, jp2]
	print(jp)
	print(L)
	
	try:
		# Crear un empleado:
		emp = Empleado('Andres','TRT',200.0)
		print(str(emp))
		print(emp)
		# objeto.metodo()
		emp.asignarProyecto('aplicacion Web','app android')
		print(emp)
		empleados = [Empleado('Andres','TRT',2000.0), \
		Empleado('Eva','Cine',2500.0), \
		Empleado('Alberto','Nacex',2000.0)]
		print(empleados)
		print('Numero de empleados: ', \
		Empleado.numeroDeEmpleados())
		
	except EmpleadoError as e:
		print(e)
		
